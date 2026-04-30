#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./run.sh <target>"
  exit 1
fi

python3 -c "from app.main import run; run('$1')"
