from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tarea
from .serializers import TareaSerializer

class IndexView(APIView):
    def get(self, request):
        context = {
            'status': True,
            'content': 'servidor activo'
        }
        return Response(context)   
    
class TareaView(APIView):
    def get(self, request):
        data = Tarea.objects.all()
        ser_data = TareaSerializer(data, many=True)
        return Response(ser_data.data)
    
    def post(self, request):
        ser_data = TareaSerializer(data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        
        return Response(ser_data.data)
        