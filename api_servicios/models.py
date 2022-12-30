from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField() # no obligatorio
    logo = models.URLField(max_length=255)
    prefix = models.CharField(max_length=3, default='NNN')

    class Meta:
        db_table = 'Api_Services'

    def __str__(self) -> str:
        return self.name