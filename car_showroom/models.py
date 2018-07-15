from django.db import models


class VehiclePart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{}. published {}\n{}, price - {},".format(
            self.id, self.pub_date,
            self.name, self.price)
