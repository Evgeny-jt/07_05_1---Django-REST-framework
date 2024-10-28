from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        Sensor.objects.create(name=request.data['name'], description=request.data['description'])
        return Response(request.data)


class Sensor_oneView(RetrieveAPIView):
    def get(self, request, pk):
        sensor = Sensor.objects.filter(sensor_id=pk).prefetch_related('sensor_id')
        ser = SensorDetailSerializer(sensor, many=True)

        return Response(ser.data)

    def patch(self, request, pk):
        wu = Sensor.objects.get(pk=pk)
        wu.description = request.data['description']
        wu.save()
        return Response(request.data)


class MeasurementView(APIView):
    def post(self, request):
        Measurement.objects.create(sensor_id=request.data['sensor'], temperature=request.data['temperature'])
        return Response({'POST': 'okey'})
