from django.db import models
# Create your models here.


class RedditPost(models.Model):
    upload_file = models.FileField(
        upload_to='tmp/uploads/', blank=False, max_length=500)
