#!/bin/bash

count=$( find . -name '*' | sed 's/.*/"&"/' | xargs  wc -l )
if [[ count > 69 ]]; then 
    exit 0
    echo "nice"
else
    echo "sus"
    exit 1