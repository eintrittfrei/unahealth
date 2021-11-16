from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Values

from serializers import ValuesSerialzier

# Create your views here.

class ValuesListView(APIView):
  
    def get(self, _request):
        values = Values.objects.all() 
        serialized_values = ValuesSerialzier(values, many=True)
        return Response(serialized_values.data, status=status.HTTP_200_OK)

    
