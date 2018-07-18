from django.db import models


class VehiclePart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, default='Add some description')
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    section = models.ForeignKey(
        'Section',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}: {}; price - {} USD. Published at: {}. Section: {}".format(
            self.id, self.name, self.price,
            str(self.pub_date)[:-9], self.section
        )


class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='Add some description')

    def __str__(self):
        return f"{self.name}: {self.description[:5]}..."