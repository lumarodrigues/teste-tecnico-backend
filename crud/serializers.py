from rest_framework import serializers
from .models import Company, Document, Signer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    signers = SignerSerializer(many=True)

    class Meta:
        model = Document
        fields = '__all__'

    def create(self, validated_data):
        signers_data = validated_data.pop('signers')
        document = Document.objects.create(**validated_data)
        for signer_data in signers_data:
            Signer.objects.create(document=document, **signer_data)
        return document
