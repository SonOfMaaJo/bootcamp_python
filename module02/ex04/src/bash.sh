!/bin/bash

python -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade build

python3 -m build
