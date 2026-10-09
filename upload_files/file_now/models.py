from django.db import models

# Create your models here.

class fileModel(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="images")
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()