from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    url  = models.URLField(max_length=200)
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to="images/")
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)


    def summary(self):
        return self.body[:105]

    def date_pretty(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title



