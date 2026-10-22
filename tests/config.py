from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass
class Config:
    base_url: str = "https://eu.store.ui.com"
    login_url: str = "https://account.ui.com/login"
    product_url: str = "https://eu.store.ui.com/eu/en/category/all-cloud-gateways"
    cart_url: str = "https://eu.store.ui.com/eu/en/checkout"
    product_name: str = "Enterprise Firewall Core"
    user: str = os.getenv("APP_USER", "")
    password: str = os.getenv("APP_PASSWORD", "")


# Load environment variables from .env file
load_dotenv()

config = Config()
