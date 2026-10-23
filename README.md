Web tests in python using pytest and playwright.

***Pre-requisities***
- python3 and pip installed
- user account with primary MFA setup to authenticator app


***Setup***
1. pip install -r requirements.txt
2. playwright install
3. create .env file in the root of the project and fill in the APP_USER, APP_PASSWORDand authenticator app secret



***Run tests***
1. Open terminal.
2. Go to the web_test_pw directory.
3. Run the command: 'pytest -v tests/test_ui.py -s'
