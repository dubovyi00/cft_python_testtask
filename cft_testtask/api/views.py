from django.shortcuts import render
from rest_framework.response import Response
from .models import *
# from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework import views
from rest_framework.response import Response

from .pic_pix import *
from urllib.request import urlopen

from pathlib import Path
import os
from http.client import InvalidURL

class WhiteBlackPixels(views.APIView):
	def get(self, request, link):
		print(link)
		try:
			rez = white_black(urlopen('http://127.0.0.1:8000/media/'+link))
		except InvalidURL:
			rez = {"err": "Имена файлов не должны содержать проблелы"}
		
		return Response(rez)
		
class HEXPixels(views.APIView):
	def get(self, request, code, link):
		print(link)
		try:
			rez = hex_pix(urlopen('http://127.0.0.1:8000/media/'+link), code)
		except InvalidURL:
			rez = {"err": "Имена файлов не должны содержать проблелы"}	

		return Response(rez)
