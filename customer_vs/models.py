from django.db import models
from datetime import datetime
# Create your models here.

class customerVSModel(models.Model):
    name=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    price=models.IntegerField()
    room_number=models.IntegerField()
    created_at=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
