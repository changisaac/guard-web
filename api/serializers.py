from rest_framework import serializers
from .models import File, Frame

class FileSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')

class FrameSerializer(serializers.ModelSerializer):
    class Meta():
        model = Frame
        fields = ('author', 'start_time', 'road_type',
        'gps_lag', 'gps_long','car','bike','man')

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = Frame
        fields = ('author', 'start_time', 'road_type',
        'gps_lag', 'gps_long','car','bike','man')