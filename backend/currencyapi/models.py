from django.db import models

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=80)
    nominal = models.IntegerField()
    value = models.DecimalField(max_digits=7, decimal_places = 4)

    def __str__(self) -> str:
        return self.name[1::]
    

class UpdateApiDateTime(models.Model):
    api_update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.api_update_time)
    
    class Meta:
        verbose_name = "DateTime of Updating API"