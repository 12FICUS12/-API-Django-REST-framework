from rest_framework import serializers
from models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
     model = Measurement
     fields = ['id_sensor', 'timestamp', 'created_at']


class ChangeSensorSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']


