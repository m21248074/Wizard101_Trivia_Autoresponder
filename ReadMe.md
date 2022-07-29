# Wizard101 Trivia Autoresponder

<p> 
	<img src="https://badgen.net/badge/Coder/m21248074/red?icon=github" />
	<img src="https://badgen.net/badge/Python/3.10.5/yellow?" />
</p>

## Quick Start

### Step 1. Install Python and ChromeDriver

Python: https://www.python.org/

ChromeDriver: https://chromedriver.chromium.org/home

### Step 2. Clone the repository

```shell
git clone git@github.com:m21248074/Wizard101_Trivia_Autoresponder.git
cd ./Wizard101_Trivia_Autoresponder
```

### Step 2. Edit the config file

Create the `config.json` file as shown below ( you can modify the `config_default.json` in the repo directly and then rename it to `config.json`):

```shell
cp config_default.json config.json
vim config.json
```

```json
{
	"username": "<Your Wizard101 Username>",
	"password": "<Your Wizard101 Password>"
}
```
- `username` and `password` correspond to the account and password on the [Wizard101](https://www.wizard101.com/) website.

### Step 3. Run the script

```shell
./start.bat
```

or

```shell
py main.py
```