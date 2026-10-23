import os
import pyotp


def get_otp_code():
    """
    Generate the current OTP code using the secret key from environment variables.

    Returns:
        str: The current OTP code.
    """
    secret = os.getenv("APP_OTP_SECRET")
    totp = pyotp.TOTP(secret)
    return totp.now()
