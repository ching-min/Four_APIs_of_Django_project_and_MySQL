from rest_framework import viewsets
 
from .serializers import GroupSerializer
from .model import Articles

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
import logging
logger = logging.getLogger(__name__)

# create a viewset			
class ArticleViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Articles.objects.all()
    # specify serializer to be used
    serializer_class = GroupSerializer
	
class ArticleCreateView(generics.CreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # User is authenticated, proceed with creating the article
            logger.debug("User is authenticated: %s", request.user)
            print("User is authenticated:", request.user)
            return super().create(request, *args, **kwargs)
        else:
            # User is not authenticated, return an authentication error response
            logger.debug("User is not authenticated")
            print("User is not authenticated")
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

	
class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = GroupSerializer
    #lookup_field="date"	
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        date = self.request.query_params.get('date', None)
        if date is not None:
            try:
                # Perform a lookup by date
                return self.queryset.get(date=date)
            except Articles.DoesNotExist:
                return None
        return None


class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = GroupSerializer
    lookup_field="date"	
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def update(self, request, *args, **kwargs):
        print(kwargs)		
        date = request.data.get('date', None)  
        updated_data = request.data.get('update_data', None)  # Extract updated data from JSON request body
        print(date)
        if date is not None:
            try:
                article = self.queryset.get(pk=date)
                # Apply the updated data to the article object
                serializer = self.get_serializer(article, data=updated_data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            except Articles.DoesNotExist:
                return Response({'error': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Missing or invalid primary key.'}, status=status.HTTP_400_BAD_REQUEST)


class ArticleRetrieveView(generics.RetrieveAPIView):
    print("retrieve")
    queryset = Articles.objects.all()
    serializer_class = GroupSerializer
    lookup_field="date"	
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def retrieve(self, request, *args, **kwargs):
        # Extract the primary key (pk) from the URL parameters
        date = request.data.get("date", None)#request.query_params.get('date', None)
        print(date)
        # Extract the column (field) name you want to retrieve from the query parameters
        column_name = "content"
        if column_name:
            try:
                article = self.queryset.get(pk=date)
                # Retrieve the specific column from the article
                column_value = getattr(article, column_name)
                return Response({column_name: column_value})
            except Articles.DoesNotExist:
                return Response({'error': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Missing column parameter.'}, status=status.HTTP_400_BAD_REQUEST)