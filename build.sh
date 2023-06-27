#!/bin/sh -e

set -xe 

source polyrythemic-sound/bin/activate

python main.py

deactivate

