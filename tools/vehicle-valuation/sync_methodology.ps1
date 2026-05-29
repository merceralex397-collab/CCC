$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillDir = Split-Path -Parent $scriptDir
$repoRoot = Split-Path -Parent (Split-Path -Parent $skillDir)
$source = Join-Path $repoRoot "referencefiles\valuation_methodology.md"
$destination = Join-Path $skillDir "references\valuation-methodology.md"

$banner = "Generated copy - edit referencefiles/valuation_methodology.md and re-run scripts/sync_methodology.ps1."
$utf8Strict = [System.Text.UTF8Encoding]::new($false, $true)
$content = [System.IO.File]::ReadAllText($source, $utf8Strict)
[System.IO.File]::WriteAllText($destination, ($banner + [Environment]::NewLine + [Environment]::NewLine + $content), $utf8Strict)
Write-Host "Synced $destination"
