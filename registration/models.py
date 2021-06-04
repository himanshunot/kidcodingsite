from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class AddInstitute(models.Model):
    inst_id = models.AutoField(primary_key=True)
    int_name = models.CharField(max_length=100)
    int_site = models.CharField(max_length=100,default="www.site.com")

    def __str__(self) -> str:
        return self.int_name

    objects = models.Manager()


class SurveyModel(models.Model):
    survey_id = models.AutoField(primary_key=True)
    institute = models.ForeignKey(AddInstitute,on_delete=models.CASCADE)
    srvy_rating = models.IntegerField()
    srvy_desc = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.srvy_desp

    objects = models.Manager()