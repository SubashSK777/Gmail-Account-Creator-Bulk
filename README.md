# Gmail Account Creator

This Python script can be used to generate random Gmail accounts. The script creates Gmail accounts using random user agents and saves the generated account information in a file.

## Requirements
- Python 3.x
- requests library (`pip install requests`)
- Selenium library (`pip install selenium`)
- Cryptography library (`pip install cryptography`)
- Fernet library (`pip install fernet`)
- Chrome WebDriver (For more information: https://sites.google.com/a/chromium.org/chromedriver/)

## Usage

1. Firstly, you will need a URL with random user agents in a file called `user-agents.txt`. See [here](https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt) for a sample list of user agents.
2. Edit `gmail_creator.py` and replace the variable `userAgentsUrl` with the URL of the user agent file.
3. Run the script: `python gmail_creator.py`.

## Caution

- This script can be used to create random Gmail accounts.
- Also, when using this script, there is no privacy and security of the created accounts. It is the user's responsibility to ensure the security of the created account information.

## Licence

This project is licensed under the MIT Licence. See the LICENSE file for more information.