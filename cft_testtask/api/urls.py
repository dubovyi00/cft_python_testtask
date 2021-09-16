from django.urls import path
from . import views

urlpatterns = [
	path('wb/<path:link>', views.WhiteBlackPixels.as_view()),
	path('hex/<str:code>/<path:link>', views.HEXPixels.as_view()),
]
