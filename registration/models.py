from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User,on_delete=CASCADE)
    srvy_rating = models.IntegerField()
    srvy_desc = models.TextField()

    def __str__(self) -> str:
        return f"{self.institute.int_name} {self.srvy_rating} {self.user.username}"

    objects = models.Manager()