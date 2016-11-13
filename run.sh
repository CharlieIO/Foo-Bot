#!/bin/env bash
while [ true ]; do
 sleep 30
 if $(ps | grep main.py)
 then
   echo "No need to start a new process"
 else
   $(python main.py &)
done
