$vol = Get-Volume -FileSystemLabel  CIRCUITPY
$volume = $vol.DriveLetter + ":\"  # Specify the volume you want to delete files from

# Get all files in the volume
$files = Get-ChildItem -Path $volume -File -Recurse -Force

# Delete each file
foreach ($file in $files) {
    Remove-Item -Path $file.FullName -Force
} 


# Get all Python files in the current folder and its subfolders
$pythonFiles = Get-ChildItem -Path ".\src" -Filter "*.*py" -Recurse

# Copy each Python file and its parent directory structure to the volume
foreach ($file in $pythonFiles) {
    $destinationDirectory = Join-Path -Path $volume -ChildPath $file.Directory.FullName.Replace($PWD.Path, "")
    New-Item -ItemType Directory -Path $destinationDirectory -Force | Out-Null
    Copy-Item -Path $file.FullName -Destination $destinationDirectory -Force
}

