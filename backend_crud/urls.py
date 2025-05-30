"""
URL configuration for backend_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from hotel.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotel.urls')),
    path('docs/', include_docs_urls(title='Hotel API Documentation')),
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('new/', ReservationCreateView.as_view(), name='reservation_create'),
    path('edit/<int:pk>/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('delete/<int:pk>/', ReservationDeleteView.as_view(), name='reservation_delete'),
]
