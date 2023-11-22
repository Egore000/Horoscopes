from django.db import models 

# Create your models here.

class Predictions(models.Model):
    zodiak_sign = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.zodiak_sign