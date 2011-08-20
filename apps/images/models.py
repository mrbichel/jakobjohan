import os
from django.db import models
import datetime

from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager


class Image(models.Model):
    file = ImageField(
        upload_to="images/",
    )

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    upload_date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    mod_date = models.DateTimeField(default=datetime.datetime.now, editable=False)

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']
        get_latest_by = 'upload_date'

    def get_absolute_url(self):
        return ''

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        if not self.title:
            self.title = os.path.basename(self.file.name)
        super(Image, self).save(*args, **kwargs)



