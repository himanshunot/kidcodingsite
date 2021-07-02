from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your views here.

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Rating", "Rating 2", "Rating 3"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[4, 4, 9, 1, 4, 5, 3],
                [4, 9, 8, 3,7, 7, 9],
                [8, 2, 9, 3, 9, 3, 6]]
# users jab bharege data tab ayega

line_chart = TemplateView.as_view(template_name='home/home.html')
line_chart_json = LineChartJSONView.as_view()

