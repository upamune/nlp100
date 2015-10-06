#!/bin/bash

cat ./hightemp.txt | split -l ${1}
