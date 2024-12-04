from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    open_id = models.IntegerField(null=False)
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_document")

    def __str__(self):
        return self.name


class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    document = models.ForeignKey("Document", on_delete=models.CASCADE, related_name="signer_document")

    def __str__(self):
        return self.name
