#!/bin/bash
python main.py
llc -filetype=obj output.ll
gcc output.o -o output
./output