from django.db import models

class Bias(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name
