# Wizard101 Trivia Autoresponder &middot; [![coder](https://badgen.net/badge/Coder/m21248074/red?icon=github)](https://github.com/m21248074) [![python version](https://badgen.net/badge/Python/3.10.5/yellow)](https://www.python.org/)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/m21248074/Wizard101_Trivia_Autoresponder/pulls)

## Quick Start

### Step 1. Download ChromeDriver and Binary Files from Releases

ChromeDriver: https://chromedriver.chromium.org/home

Current lastest version is [1.0.0](https://github.com/m21248074/Wizard101_Trivia_Autoresponder/releases)

### Step 2. Execute the EXE File and Enjoy It! 

## Manual Start

### Step 1. Install Python and ChromeDriver

Python: https://www.python.org/

ChromeDriver: https://chromedriver.chromium.org/home

### Step 2. Clone the repository

```shell
git clone git@github.com:m21248074/Wizard101_Trivia_Autoresponder.git
cd ./Wizard101_Trivia_Autoresponder
```

### Step 3. Install the Python Dependencies

```shell
pip install eel selenium
```

### Step 4. Create the config file

Create the `config.json` file as shown below ( you can modify the `config_default.json` in the repo directly and then rename it to `config.json`):

```shell
cp config_default.json config.json
```

### Step 5. Run the script

```shell
./start.bat
```

or

```shell
py main.py
```

## Pack Your Own

```shell
python -m eel main.py web --onefile --noconsole --hidden-import=queue -F -w
pyinstaller main.spec
```