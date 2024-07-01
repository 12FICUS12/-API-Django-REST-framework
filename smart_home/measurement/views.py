# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView

from smart_home.measurement.models import Sensor, Measurement
from smart_home.measurement.serializers import SensorSerializer, MeasurementSerializer, ChangeSensorSerializer


# получение списка датчиков
class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# получение списка измерений/ добавить
class ChangeSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# измерить датчик / посмотреть
class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#получить информацию по конкретному датчику
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = ChangeSensorSerializer



