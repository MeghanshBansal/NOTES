from django.db import models
import hashlib
import datetime
import time
# Create your models here.


def createHash():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    return hash.hexdigest()[:-10]


class Note(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          default=createHash, max_length=100, )
    title = models.CharField(max_length=50, )
    content = models.TextField(max_length=5000, )
    dateTime = models.CharField(
        null=False, default=str(datetime.datetime.now()), max_length=30)

    def __str__(self) -> str:
        return "{title}_{date}___{id}".format(title=self.title, date=self.dateTime, id=self.id)
