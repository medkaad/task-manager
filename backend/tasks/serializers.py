from rest_framework import serializers
from .models import Project, Task
from .utils import predict_priority

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['priority']

    def create(self, validated_data):
        text = f"{validated_data.get('title', '')} {validated_data.get('description', '')}"
        validated_data['priority'] = predict_priority(text)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        text = f"{validated_data.get('title', instance.title)} {validated_data.get('description', instance.description)}"
        instance.priority = predict_priority(text)
        return super().update(instance, validated_data)
