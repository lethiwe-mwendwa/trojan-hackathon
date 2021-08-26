from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class donee(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    message = models.TextField()
    email = models.EmailField()
    contact = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def snippet(self):
        return self.message[:150] + '...'
