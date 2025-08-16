@echo off
set "CIRCUITPY_DRIVE="

for /f "tokens=1,2" %%a in ('powershell -Command "Get-CimInstance -ClassName Win32_Volume | Where-Object { $_.Label -eq 'CIRCUITPY' } | Select-Object DriveLetter"') do (
    if "%%a"=="DriveLetter" (
        set CIRCUITPY_DRIVE=%%b:
    )
)
if defined CIRCUITPY_DRIVE (
    echo CircuitPython drive found at %CIRCUITPY_DRIVE%
    start "" "C:\Users\morot\AppData\Local\Programs\Microsoft VS Code\code.exe" ".\open_colorimeter_firmware_win.code-workspace"
) else (
    echo CircuitPython drive not found. Please connect the device.
)

pause