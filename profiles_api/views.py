from rest_framework.views import APIView
from rest_framework.response import Response


class ApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns Our APIView Feature"""
        an_apiview = [
            'Uses HTTP functions (get, post, patch, put, delete)',
            'Is similar to a Django View',
            'Is mapped main to URLs',
        ]
        
        return Response({'message': 'Hi Im an API', 'an_apiview': an_apiview})