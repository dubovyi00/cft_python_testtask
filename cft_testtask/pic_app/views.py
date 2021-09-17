from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
import requests


def main_view(request):
  
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
  
		if form.is_valid():
			form.save()
			
			if form.cleaned_data['mode'] == 'WB':
				# This is not logical, I suppose, but it is enough for demonstration 
				results = requests.get('http://127.0.0.1:8000/api/wb/images/'+str(form.cleaned_data['src'])).json()
				request.session['temp_data'] = results
				
				return redirect('results_wb') 
			elif form.cleaned_data['mode'] == 'HEX':
				results = requests.get('http://127.0.0.1:8000/api/hex/'+str(form.cleaned_data['color'])+'/images/'+str(form.cleaned_data['src'])).json()
				results['color'] = '#'+str(form.cleaned_data['color'])
				request.session['temp_data'] = results
				
				return redirect('results_hex') 
			
	else: 
		
		print()
		form = ImageForm()
        	
	return render(request, 'index.html', {'form' : form})
  
  
def results_wb(request):
	print(request.session['temp_data'])
	r = request.session['temp_data']
	if 'err' not in r.keys():
		
		if r['which_is'] == "White":
			word = "белых"
		elif r['which_is'] == "Black":
			word = "чёрных"
		else:
			word = "и тех, и других"
		return HttpResponse("Количество белых пикселей: "+str(r['wpx'])+" ("+str(r['wper'])+"""%) <br> 
		Количество чёрных пикселей: """+str(r['bpx'])+" ("+str(r['bper'])+"""%) <br> 
		Больше всего """+word+"""<br>
		<a href="http://127.0.0.1:8000">Вернуться</a>
		""")
	else:
		return HttpResponse(r['err']+"""
		<br>
		<a href="http://127.0.0.1:8000">Вернуться</a>
		""")
		
def results_hex(request):
	print(request.session['temp_data'])
	r = request.session['temp_data']
	if 'err' not in r.keys():
		#return HttpResponse(str(r))
		return HttpResponse("Количество пикселей цвета "+str(r['color'])+": "+str(r['hexpix'])+" ("+str(r['hexper'])+"""%) <br> 
		<div style="background-color: """+ str(r['color'])+"""; ">
			<p>Фон этой строки окрашен в выбранный вами цвет</p>
		</div>
		<a href="http://127.0.0.1:8000">Вернуться</a>
		""")
	else:
		return HttpResponse(r['err']+"""
		<br>
		<a href="http://127.0.0.1:8000">Вернуться</a>
		""")
