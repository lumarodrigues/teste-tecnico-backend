import base64
import requests
from rest_framework import serializers
from django.conf import settings
from .models import Document, Signer, Company
import os


class SignerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)


class DocumentSerializer(serializers.ModelSerializer):
    signer_document = SignerSerializer(many=True, required=True)
    name = serializers.CharField(max_length=255, required=True)
    created_by = serializers.CharField(max_length=255, required=True)
    pdf_url = serializers.URLField(required=True)

    class Meta:
        model = Document
        fields = [
            'id', 'name', 'created_by', 'pdf_url', 'signer_document',
        ]

    def create(self, validated_data):
        signer_data = validated_data.pop('signer_document', [])

        try:
            company = Company.objects.last()
        except Company.DoesNotExist:
            raise serializers.ValidationError(f"Company not found.")

        pdf_url = validated_data['pdf_url']
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code != 200:
            raise serializers.ValidationError(
                f"Error downloading PDF: {pdf_response.status_code} - {pdf_response.text}"
            )

        base64_pdf = base64.b64encode(pdf_response.content).decode('utf-8')

        signers = [{"name": signer['name'], "email": signer['email']} for signer in signer_data]

        document_data = {
            "name": validated_data['name'],
            "base64_pdf": base64_pdf,
            "signers": signers,
        }

        zapsign_url = os.getenv("ZAPSIGN_URL")
        headers = {
            "Authorization": f"Bearer {company.api_token}",
            "Content-Type": "application/json"
        }

        response = requests.post(zapsign_url, json=document_data, headers=headers)

        if response.status_code != 200:
            raise serializers.ValidationError(f"Error on document creation: {response.text}")

        response_data = response.json()
        open_id = response_data.get('open_id')

        if not open_id:
            raise serializers.ValidationError("Field 'open_id' not returned by the API.")

        document = Document.objects.create(
            name=validated_data['name'],
            created_by=validated_data['created_by'],
            pdf_url=validated_data['pdf_url'],
            token=response_data.get('token'),
            open_id=open_id,
            company_id=company.id,
        )

        for signer in signer_data:
            Signer.objects.create(document=document, **signer)

        return document

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.pdf_url = validated_data.get('pdf_url', instance.pdf_url)
        signer_data = validated_data.get('signer_document', [])

        if signer_data is not None:
            instance.signer_document.all().delete()

            for signer in signer_data:
                Signer.objects.create(document=instance, **signer)

        instance.save()
        return instance
