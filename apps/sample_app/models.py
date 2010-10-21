from django.db import models

from managers import SampleManager

class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    processed = models.BooleanField(default=False)

    objects = SampleManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name",]
