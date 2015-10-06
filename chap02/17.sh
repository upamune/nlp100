#!/bin/bash

cat hightemp.txt | cut -f 1 | sort | uniq

