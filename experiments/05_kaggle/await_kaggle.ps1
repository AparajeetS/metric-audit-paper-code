$id = "aparajeetshadangi/cei-mbe-cifar10-grid"
$kaggle = "C:\Users\apara\AppData\Local\Python\pythoncore-3.14-64\Scripts\kaggle.exe"
while ($true) {
    $status = & $kaggle kernels status $id
    Write-Host $status
    if ($status -match "complete" -or $status -match "KernelWorkerStatus.COMPLETE") {
        Write-Host "Kernel complete! Downloading output..."
        & python download_kaggle.py
        break
    }
    if ($status -match "error" -or $status -match "cancel" -or $status -match "KernelWorkerStatus.ERROR") {
        Write-Host "Kernel failed or cancelled."
        exit 1
    }
    Start-Sleep -Seconds 30
}
