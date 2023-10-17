from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to='image')
    slug = models.SlugField(default='', blank=True)
    des = models.CharField(max_length=150)

    def __str__(self):
        return self.des

