from django.urls import path

from smart_home.measurement.views import SensorCreateView, MeasurementCreateView, ChangeSensorView, SensorView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/update/<pk>/', ChangeSensorView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
