from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=255)
    value = models.PositiveIntegerField(default=0)
    icon_file = models.ImageField(upload_to='media', null=True, blank=True)
    icon_url = models.URLField(null=True)

    def __str__(self):
        return self.name
