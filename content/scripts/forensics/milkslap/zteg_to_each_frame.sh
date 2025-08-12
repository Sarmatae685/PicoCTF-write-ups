#!/bin/bash

echo "==zsteg scan=="

for frame in frame_*.png; do 
  if zsteg $frame 2>/dev/null | grep -iE "pico|ctf|flag"; then
  	echo "FOUND FLAG"
  	zsteg $frame 2>/dev/null | grep -iE "pico|ctf|flag"
  else
  	echo "NOTHING YET"
  fi
done
