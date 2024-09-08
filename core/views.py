from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


from api.models import Users
from .models import FileLog, DirectoryLog
from .serializer import FileSerializer, DirectorySerializer



class FileOps(ModelViewSet):
    # Defaults
    queryset = FileLog.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    dir_serializer_class = DeprecationWarning
    
    @action(detail=False, methods=['post'])
    def userfiles(self, request):
        user = Users.objects.get(user_id = request.data.get('userid'))
        response = self.queryset.filter(owner=user)
        print(response)
        response = FileSerializer(response, many=True).data
        return Response(response)
        
    @action(detail=False, methods=['post'])
    def userdirectories(self, request):
        user = Users.objects.get(user_id = request.data.get('userid'))
        directories = DirectoryLog.objects.filter(owner=user)
        
        response = DirectorySerializer(directories, many=True).data
        return Response(response)
    
    def get_view_name(self):
        return "File Operations"
    