# Quick start
```bash
git clone --recursive https://github.com/AndrewSultan/freqml.git
cd freqml
# ./setup.sh in the future
git checkout master
python3 -m venv .env
source .env/bin/activate
python3 -m pip install --upgrade pip
pip install -e .
pip install ipykernel
ipython kernel install --user --name=freqml
cd freqtrade
git checkout develop
python3 -m pip install -e .
```
