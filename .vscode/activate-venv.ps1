$workspaceRoot = Split-Path -Parent $PSScriptRoot
$venvPath = Join-Path $workspaceRoot ".venv"
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
$uvBin = "C:\Users\EliteBook\.local\bin"

if (Test-Path $uvBin) {
    $pathParts = $env:PATH -split ";"
    if ($pathParts -notcontains $uvBin) {
        $env:PATH = "$uvBin;$env:PATH"
    }
}

if (-not (Test-Path $activateScript)) {
    Write-Warning "Project virtual environment was not found at: $venvPath"
    return
}

$resolvedVenvPath = (Resolve-Path $venvPath).Path
if ($env:VIRTUAL_ENV -ne $resolvedVenvPath) {
    . $activateScript
}

$env:VIRTUAL_ENV_PROMPT = ".venv"
