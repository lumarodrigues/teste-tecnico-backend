from crud.models import Company
from crud.serializers import DocumentSerializer
from django.urls import reverse


def test_create_document(db, client, company, document_url, api_url):
    payload = {
        "name": "Contrato",
        "created_by": "Test User 1",
        "pdf_url": document_url,
        "signer_document": [
            {
                "name": "Test User 2",
                "email": "testuser2@example.com"
            },
            {
                "name": "Test User 3",
                "email": "testuser3@example.com"
            }
        ]
    }
    response = client.post(reverse("document-list"), payload, content_type="application/json")
    assert response.status_code == 201


def test_edit_document(client, document):
    payload = {
        "signer_document": [
            {
                "name": "Test User 2",
                "email": "testuser2@example.com"
            },
            {
                "name": "Test User 4",
                "email": "testuser4@example.com"
            }
        ]
    }
    response = client.patch(reverse("document-detail", args=(document.pk,)), payload, content_type="application/json")
    assert response.status_code == 200


def test_delete_document(client, document):
    response = client.delete(reverse("document-detail", args=(document.pk,)), content_type="application/json")
    assert response.status_code == 204


def test_create_document_failure(db, client):
    payload = {
        "name": "Contrato",
        "created_by": "Test User 1",
        "pdf_url": "",
        "signer_document": [
            {
                "name": "Test User 2",
                "email": "testuser2@example.com"
            }
        ]
    }
    response = client.post(reverse("document-list"), payload, content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {'pdf_url': ['This field may not be blank.']}
