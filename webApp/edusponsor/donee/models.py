from django.db import models

# Create your models here.
class donee(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    contact = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True)
    #  slug = models.SlugField(unique=True) how to add slugs without one off null value in cmd
    # add in thumbnail later
    # add in author later

    def __str__(self):
        return self.name

    def snippet(self):
        return self.message[:200] + '...'