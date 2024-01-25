from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)
# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

    def get(self, request, *args, **kwargs):
        # Accessing headers
        authorization_header = request.headers.get('Authorization')

        # Do something with the header
        if authorization_header:
            print(f"Authorization header value: {authorization_header}")
        logger.info(f"Headers: {request.headers}")
        # Your view logic here
        return Response({'message': 'Hello, world!'})