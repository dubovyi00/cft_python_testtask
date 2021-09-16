from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', hotel_image_view, name = 'index'),
	path('results_wb', results_wb, name = 'results_wb'),
	path('results_hex', results_hex, name = 'results_hex'),
]
