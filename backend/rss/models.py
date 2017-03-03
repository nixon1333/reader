from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FeedsList(models.Model):
    url = models.TextField()
    status = models.IntegerField(default=1)
    name = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name
