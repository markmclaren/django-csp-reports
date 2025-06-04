from django.urls import path

from .views import report_csp

urlpatterns = [
    path('report/', report_csp, name='report_csp'),
]
