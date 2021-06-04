from django.contrib import admin
from .models import AddInstitute, SurveyModel
# Register your models here.

@admin.register(AddInstitute)
class addinstitute(admin.ModelAdmin):
    list_display = ('inst_id','int_name')

@admin.register(SurveyModel)
class survey(admin.ModelAdmin):
    list_display = ('institute','srvy_rating')