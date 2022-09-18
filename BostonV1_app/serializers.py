from rest_framework import serializers
from BostonV1_app.models import Server_Data,CPU_Data,RAM_Data,Disk_Data

class server_data_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Server_Data
        fields = '__all__'

class cpu_data_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = CPU_Data
        fields = '__all__'

class ram_data_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = RAM_Data
        fields = '__all__'

class disk_data_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Disk_Data
        fields = '__all__'