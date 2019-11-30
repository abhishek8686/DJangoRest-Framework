from django.db import models

class Lead(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    message=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
