import pytest
from model_bakery import baker
import os


@pytest.fixture
def company(db):
    return baker.make("Company")


@pytest.fixture
def document_url(responses):
    url = "https://www.documenttest/test.pdf"
    responses.add(responses.GET, url, body="")
    return url


@pytest.fixture
def api_url(responses):
    url = os.getenv("ZAPSIGN_URL")
    responses.add(responses.POST, url, body='{"open_id": "1234", "token": "a1b2c3d4"}', content_type="application/json")
    return url


@pytest.fixture
def document(db):
    return baker.make("Document")
