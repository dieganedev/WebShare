from django.db import models
from django import forms

class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True    

# Create your models here.

class Liste(TimespamtedModel):
    title = models.CharField(max_length=50)
    file = models.FileField()
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)    

    def __str__(self):
        return self.title

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))



