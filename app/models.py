from django.db import models
from django_pandas.managers import DataFrameManager

class MyModel(models.Model):
    full_name = models.CharField(max_length=25)
    age = models.IntegerField()
    department = models.CharField(max_length=3)
    wage = models.FloatField()

    objects = DataFrameManager()


class LongTimeSeries(models.Model):
    date_ix = models.DateTimeField()
    series_name = models.CharField(max_length=100)
    value = models.FloatField()

    objects = DataFrameManager()

class PivotData(models.Model):
    row_col_a = models.CharField(max_length=15)
    row_col_b = models.CharField(max_length=15)
    row_col_c = models.CharField(max_length=15)
    value_col_d = models.FloatField()
    value_col_e = models.FloatField()
    value_col_f = models.FloatField()

    objects = DataFrameManager()