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
from .views import ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ArticleRetrieveView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
	#path('admin/', admin.site.urls),
	path('api/token/', TokenObtainPairView.as_view(), name='obtain_jwt_token'),  # Obtain JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_jwt_token'),  # Refresh JWT token   
	path('api/articles/create/', ArticleCreateView.as_view(), name='article-create'), # create a new article
	path('api/articles/delete/', ArticleDeleteView.as_view(), name='article-delete'), # delete an article by "date"
	path('api/articles/update/', ArticleUpdateView.as_view(), name='article-update'), # modify an article, search by "date"
	path('api/articles/retrieve/', ArticleRetrieveView.as_view(), name='article-retrieve'), # retrieve the content of an article, search by "date"

]
