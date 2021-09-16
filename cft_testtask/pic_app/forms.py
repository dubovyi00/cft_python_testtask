from django import forms
from .models import *
  
class ImageForm(forms.ModelForm):
  
    class Meta:
        model = Pictures
        fields = ['src', 'mode', 'color']
        
        #self.src.label = "Выберите картинку"
        #self.mode.label = "Режим"
        #self.mode.color = "Код цвета #"
