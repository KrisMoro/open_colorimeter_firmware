#!/bin/bash

# Define the source directory (your project files)
SRC_DIR="./src/"

# Define the destination directory (your CircuitPython drive)
# Replace "CIRCUITPY" with the name of your CircuitPython drive
DEST_DIR="/Volumes/CIRCUITPY/"

# Check if the destination directory exists
if [ ! -d $DEST_DIR ]; then
  echo "Error: Destination directory does not exist."
  exit 1
fi

#empty the destination directory
rm -rf $DEST_DIR/*

# Use rsync to copy the files
rsync -r $SRC_DIR $DEST_DIR