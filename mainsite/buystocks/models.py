from django.db import models


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=4)
    multiple = models.IntegerField(min_value=1)


    def current_price(self):
        # TODO: API call to yfinance
        pass
