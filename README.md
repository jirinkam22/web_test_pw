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
3. Run teh command: 'pytest -v tests/test_ui.py -s' or 'pytest -v -m semi_automated -s'
4. Please, keep in mind that the test_add_product_to_cart is semi-automated and requires
manual intervention. During the run, a message will appear in the terminal, where the test runs and
you will be prompted to approve the login in the UI Verify app for each login attempt, press Enter
in the terminal after the approval.
