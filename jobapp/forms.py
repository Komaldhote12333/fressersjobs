from django import forms
from .models import *

class Location(forms.ModelForm):
    class Meta:
        model = location
        fields = "__all__"
        
        
class Pakage(forms.ModelForm):
    class Meta:
        model = pakage
        fields = "__all__"        
        
class Jobsdis(forms.ModelForm):
    class Meta:
        model = jobsdis
        fields = "__all__"        
        
        
class Movee(forms.ModelForm): 
    class Meta:
        model = movee
        fields = "__all__"   
        
        
               