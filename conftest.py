import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL", "https://example.com")
    if not url.startswith("http"):
        raise ValueError("BASE_URL must include scheme, e.g. https://")
    return url