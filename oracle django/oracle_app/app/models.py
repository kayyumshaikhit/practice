from django.db import models

# Create your models here.

class FileModel(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="uploads")

    def __str__(self) -> str:
        return super().__str__()