from django.db import models


class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True    

# Create your models here.

class Poste(TimespamtedModel):
    title = models.CharField(max_length=50)
    file = models.FileField()
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)    

    def __str__(self):
        return self.title



