from django.db import models


class URLDomains(models.Model):
    title = models.CharField(max_length=40, verbose_name="Назва домену")
    slug = models.SlugField()

    def __str__(self):
        return self.title


class UserUrls(models.Model):
    user_id = models.GenericIPAddressField()
    long_url = models.URLField()
    shorten_url = models.URLField()
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='site-image/%Y/%m/%d', null=True, default=None)

    def __str__(self):
        return self.long_url

