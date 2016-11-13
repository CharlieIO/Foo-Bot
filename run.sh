#!/bin/env bash
while :
do
  sleep 3
  if pgrep -f "main.py" > /dev/null
  then
    echo "No need to start a new process"
    sleep 30
  else
    $(python main.py &) || echo "Python error!" && continue
  fi
done
