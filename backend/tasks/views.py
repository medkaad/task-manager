from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()

        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)

        return queryset