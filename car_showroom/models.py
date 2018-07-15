from django.db import models


class VehiclePart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{}: {}; price - {} USD. Published at: {}".format(
            self.id, self.name,
            self.price, str(self.pub_date)[:-9])
