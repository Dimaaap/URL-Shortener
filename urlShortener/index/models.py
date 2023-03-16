from django.db import models


class URLDomains(models.Model):

    title = models.CharField(max_length=40, verbose_name="Назва домену")
    slug = models.SlugField()


    def __str__(self):
        return self.title

