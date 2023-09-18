"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from .views import ArticleViewSet, ObtainJWTToken
from .views import ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ArticleRetrieveView
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
	#path('items/', ArticleViewSet.as_view(), name='mymodel-list-create'),
	#path('items/<int:pk>/', ArticleViewSet.as_view(), name='item-retrieve-update-destroy'),
    #path('items/', ArticleViewSet, name='mymodel-list-create'),
	#path('items/<int:pk>/', ArticleViewSet, name='item-retrieve-update-destroy'),
	#path('get-token/', ObtainJWTToken.as_view(), name='get-token'),
    # Define more URL patterns for your other views here
    path('admin/', admin.site.urls),
	#path('', include('api_views.urls'))
	#path('api/token/', obtain_jwt_token, name='obtain_jwt_token'),  # Obtain JWT token
    #path('api/token/refresh/', refresh_jwt_token, name='refresh_jwt_token'),  # Refresh JWT token
	path('api/token/', TokenObtainPairView.as_view(), name='obtain_jwt_token'),  # Obtain JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_jwt_token'),  # Refresh JWT token   
	path('api/articles/create/', ArticleCreateView.as_view(), name='article-create'),
	path('api/articles/delete/', ArticleDeleteView.as_view(), name='article-delete'),
	path('api/articles/update/', ArticleUpdateView.as_view(), name='article-update'),
	path('api/articles/retrieve/', ArticleRetrieveView.as_view(), name='article-retrieve'),

]
