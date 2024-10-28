from django.urls import path

from measurement.views import MeasurementView, SensorView, Sensor_oneView

urlpatterns = [
    path('measurements/', MeasurementView.as_view()),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', Sensor_oneView.as_view()),

]
