param(
    [ValidateSet("personal", "organization", "combined")]
    [string]$Profile = "personal",

    [string]$Organization = "",

    [ValidateSet("both", "claude", "codex")]
    [string]$Agents = "both"
)

$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Renderer = Join-Path $Root "scripts/render-instructions.py"

$Python = Get-Command py -ErrorAction SilentlyContinue
if ($Python) {
    $PythonCommand = "py"
    $PythonArgs = @("-3")
} else {
    $Python = Get-Command python -ErrorAction SilentlyContinue
    if (!$Python) {
        throw "Python 3 is required. Install Python and retry."
    }
    $PythonCommand = "python"
    $PythonArgs = @()
}

if ($Profile -in @("organization", "combined") -and !$Organization) {
    throw "Specify -Organization for this profile."
}

Write-Host "AI Engineering Standards Bootstrap"
Write-Host "Repository: $Root"
Write-Host "Profile: $Profile"
Write-Host "Organization: $Organization"
Write-Host "Agents: $Agents"

$Arguments = $PythonArgs + @(
    $Renderer,
    "--repo-root", $Root,
    "--profile", $Profile,
    "--org", $Organization,
    "--agents", $Agents
)

& $PythonCommand @Arguments

if ($LASTEXITCODE -ne 0) {
    throw "Standards bootstrap failed with exit code $LASTEXITCODE"
}

Write-Host "Bootstrap completed successfully."

