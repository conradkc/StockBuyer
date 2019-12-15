from django.db import models
from django.utils import timezone

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    wallet = models.DecimalField(decimal_places= 7)

    def get_revenue(self):
        # TODO: calculate revenue


class Stock(models.Model):
    name = models.CharField(max_length=4)
    multiple = models.IntegerField(min_value=1)
    cost = models.DecimalField(decimal_places= 5)
    date = models.DateTimeField(default=timezone.now())
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)

    def current_price(self):
        # TODO: API call to yfinance
        pass


