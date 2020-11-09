from django.db import models


# Create your models here.
class EmpModel(models.Model):
    empid = models.CharField(max_length=20)
    empname = models.CharField(max_length=40)
    email = models.EmailField()
    phoneno = models.CharField(max_length=12)

    class Meta:
        db_table = "employees"  # db table will have this name
