import os
import pandas as pd
import numpy as np
import pingouin as pg
from scipy.stats import pearsonr, spearmanr
from dataclasses import dataclass
import matplotlib.pyplot as plt
import seaborn as sns
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

@dataclass
class MBEReport:
    metric_name: str
    baseline_name: str
    absolute_r: float
    absolute_p: float
    partial_r: float
    partial_p: float
    is_loss_proxy: bool

class MBEEvaluator:
    """
    The Marginal Baseline Eval (MBE) framework.
    Evaluates whether a proposed representation metric offers independent
    structural insight beyond a trivial baseline (e.g. early validation loss).
    """
    
    def __init__(self, metric_name: str = "Proposed Metric", baseline_name: str = "Validation Loss"):
        self.metric_name = metric_name
        self.baseline_name = baseline_name
        
    def evaluate(self, metric_vals: np.ndarray, baseline_vals: np.ndarray, target_vals: np.ndarray, 
                 alpha: float = 0.05, output_dir: str = "mbe_reports") -> MBEReport:
        """
        Runs Stage 1 (Absolute Correlation) and Stage 4 (Partial Correlation).
        """
        console.print(Panel(f"[bold cyan]Marginal Baseline Eval (MBE) - {self.metric_name}[/bold cyan]"))
        
        # Stage 1: Absolute Correlation (Does it predict the target at all?)
        # We use Spearman rank correlation as the primary measure for structural metrics
        abs_r, abs_p = spearmanr(metric_vals, target_vals)
        
        # Stage 4: Partial Correlation (Does it beat the baseline?)
        # Partial correlation requires linear controls, so we use Pearson on the ranks if desired,
        # but pingouin partial_corr handles linear partials well. We'll use pingouin.
        df = pd.DataFrame({
            'Target': target_vals,
            'Metric': metric_vals,
            'Baseline': baseline_vals
        })
        
        pcorr = pg.partial_corr(data=df, x='Metric', y='Target', covar='Baseline', method='spearman')
        part_r = pcorr['r'].values[0]
        part_p = pcorr['p_val'].values[0]
        
        is_proxy = part_p > alpha
        
        report = MBEReport(
            metric_name=self.metric_name,
            baseline_name=self.baseline_name,
            absolute_r=abs_r, absolute_p=abs_p,
            partial_r=part_r, partial_p=part_p,
            is_loss_proxy=is_proxy
        )
        
        self._print_rich_report(report)
        self._generate_plots(df, report, output_dir)
        
        return report

    def _print_rich_report(self, r: MBEReport):
        table = Table(title="MBE Evaluation Results", show_header=True, header_style="bold magenta")
        table.add_column("Stage", style="dim", width=20)
        table.add_column("Test", width=40)
        table.add_column("Correlation", justify="right")
        table.add_column("p-value", justify="right")
        table.add_column("Verdict", justify="center")
        
        # Absolute
        abs_verdict = "[bold green]PASS[/bold green]" if r.absolute_p < 0.05 else "[bold red]FAIL[/bold red]"
        abs_p_str = f"[green]{r.absolute_p:.2e}[/green]" if r.absolute_p < 0.05 else f"[red]{r.absolute_p:.2e}[/red]"
        table.add_row("1: Absolute", f"Correlation with Final Target", f"{r.absolute_r:.3f}", abs_p_str, abs_verdict)
        
        # Partial
        part_verdict = "[bold red]FAIL[/bold red]" if r.is_loss_proxy else "[bold green]PASS[/bold green]"
        part_p_str = f"[red]{r.partial_p:.2e}[/red]" if r.is_loss_proxy else f"[green]{r.partial_p:.2e}[/green]"
        table.add_row("4: MBE Control", f"Controlling for {r.baseline_name}", f"{r.partial_r:.3f}", part_p_str, part_verdict)
        
        console.print(table)
        
        if r.is_loss_proxy:
            console.print(f"[bold red]DIAGNOSIS: {r.metric_name} is a disguised Loss Proxy.[/bold red]")
            console.print(f"It provides NO independent predictive signal beyond {r.baseline_name}.\n")
        else:
            console.print(f"[bold green]DIAGNOSIS: {r.metric_name} provides independent structural insight![/bold green]\n")

    def _generate_plots(self, df: pd.DataFrame, r: MBEReport, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(f"MBE Report: {r.metric_name}", fontsize=16, fontweight='bold')
        
        # Plot 1: Metric vs Target (Absolute)
        sns.regplot(ax=axes[0], data=df, x='Metric', y='Target', scatter_kws={'alpha':0.6, 's':80}, color='indigo')
        axes[0].set_title(f"Stage 1: Absolute Correlation\nρ = {r.absolute_r:.3f} (p = {r.absolute_p:.2e})", fontsize=14)
        axes[0].set_xlabel(r.metric_name, fontsize=12)
        axes[0].set_ylabel("Final Target (e.g., Accuracy)", fontsize=12)
        
        # Plot 2: Bar chart of correlation collapse
        labels = ['Absolute\n(Uncontrolled)', f'Marginal\n(Controlling {r.baseline_name})']
        vals = [abs(r.absolute_r), abs(r.partial_r)]
        colors = ['#2ecc71' if r.absolute_p < 0.05 else '#e74c3c', 
                  '#2ecc71' if not r.is_loss_proxy else '#e74c3c']
        
        axes[1].bar(labels, vals, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        axes[1].set_ylim(0, 1.0)
        axes[1].set_ylabel("Absolute Magnitude of Spearman ρ", fontsize=12)
        axes[1].set_title("Stage 4: Predictive Power Collapse", fontsize=14)
        
        for i, v in enumerate(vals):
            axes[1].text(i, v + 0.02, f"|ρ|={v:.3f}", ha='center', fontsize=12, fontweight='bold')

        plt.tight_layout()
        save_path = os.path.join(output_dir, f"mbe_report_{r.metric_name.replace(' ', '_')}.png")
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        console.print(f"[dim]Generated graphical report at: {save_path}[/dim]")
