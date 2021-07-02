from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from registration.models import AddInstitute,SurveyModel
from django.contrib.auth import get_user_model

# Create your views here.

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return  labels for the x-axis."""
        
        User = get_user_model()
        return [item.username for item in  User.objects.all()]
       

    def get_providers(self):
        """Return names of datasets."""
        return [item.int_name for item in AddInstitute.objects.all()] 

    def get_data(self):
        """Return 3 datasets to plot."""
        total=[]
        for insti in AddInstitute.objects.all():
            print(insti)
            ratings = []
            survey = SurveyModel.objects.filter(institute=insti)
            if len(survey)>0:
                for item in survey:
                    print(item.institute.int_name)
                    ratings.append(item.srvy_rating)
            total.append(ratings)
        print(total)
        return total
# users jab bharege data tab ayega

line_chart = TemplateView.as_view(template_name='home/home.html')
line_chart_json = LineChartJSONView.as_view()

