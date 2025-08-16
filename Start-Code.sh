#!/bin/bash

CIRCUITPY_PATH="/Volumes/CIRCUITPY"

if [ -d "$CIRCUITPY_PATH" ]; then
    echo "CircuitPython drive found at $CIRCUITPY_PATH"
    open -a "Visual Studio Code" "/Users/YourUser/Documents/projects/mac-workspace.code-workspace"
else
    echo "CircuitPython drive not found. Please connect the device."
fi