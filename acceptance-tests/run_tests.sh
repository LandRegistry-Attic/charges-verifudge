#!/bin/bash

set -e

#Remove any error screenshots from previous runs
rm -f sshot*

bundle install

if [ -z "$1"]
  then
  #If no arguments supplied
  cucumber --tags ~@wip
else
  #If arguments supplied
  cucumber $1
fi
