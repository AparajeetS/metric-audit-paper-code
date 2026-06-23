import torch
import math
import numpy as np

def compute_fim_norm(model, loss_fn, inputs, targets):
    """
    Computes Gradient Effective Rank (FIM_norm) via the dual Gram matrix.
    This exactly implements the mathematical formulation from the MBE paper.
    """
    N = inputs.shape[0]
    
    # We need per-sample gradients. Since standard PyTorch accumulates,
    # we compute it one by one for exactness. (In practice, functorch/vmap is faster, 
    # but a simple loop is highly readable for a demonstration.)
    
    grads = []
    model.eval() # ensure no batchnorm tracking during this
    
    for i in range(N):
        x = inputs[i:i+1]
        y = targets[i:i+1]
        
        loss = loss_fn(model(x), y)
        model.zero_grad()
        loss.backward()
        
        # Flatten all parameters' gradients into a single vector
        g_vec = torch.cat([p.grad.flatten() for p in model.parameters() if p.grad is not None])
        grads.append(g_vec.detach())
        
    G = torch.stack(grads) # shape: (N, P)
    
    # The Dual Gram Matrix
    S_dual = (1.0 / N) * torch.matmul(G, G.T) # shape: (N, N)
    
    # Eigendecomposition
    eigenvalues = torch.linalg.eigvalsh(S_dual)
    eigenvalues = eigenvalues[eigenvalues > 1e-12] # numerical noise floor
    
    if len(eigenvalues) == 0:
        return 1.0 # Max normalized rank
        
    # Shannon entropy of normalized spectrum
    p = eigenvalues / eigenvalues.sum()
    H = -(p * torch.log(p)).sum().item()
    
    erank = math.exp(H)
    fim_norm = erank / N
    
    return fim_norm
