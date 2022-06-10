from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"

    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=256, null=False)
