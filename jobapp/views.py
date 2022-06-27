from django.shortcuts import render
from .forms import *
from .models import *


     

def index(request):
    joblists = jobsdis.objects.all()
    salary= pakage.objects.all()
    cateid = request.GET.get('salaryid')
    salaryidd = request.GET.get('salaryidd')
    if cateid:
        joblists = jobsdis.objects.filter(pakages=cateid)
    elif salaryidd:
        joblists = jobsdis.objects.all()
            
    else:
        joblists = jobsdis.objects.all()
            
    data={
        "joblists":joblists,
        "salary":salary,
    }  
    print(joblists)
    
    return render(request,'index.html',data)


    
# Create your views here.
def adminlog(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
   
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
 
      
     }
    print(emp)
    return render(request,'admin.html',data)
   
def insertlocation(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
      
     }
    if request.method == "POST":
        places = Location(request.POST)
        places.save()
        return render(request,'admin.html',data)
    else:
        return render(request,'admin.html',data)
    



def insertjob(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
      
     }
    
    if request.method == "POST":
        nokari =Jobsdis(request.POST)
        if nokari.is_valid():   
            nokari.save()
            return render(request,'admin.html',data)
        else:
            return render(request,'admin.html')
    else:
        return render(request,'admin.html')


def insertmoves(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
      
     }
    if request.method == "POST":
        picture = Movee(request.POST) 
        picture.save()  
        return render(request,'admin.html',data)
    else:
        return render(request,'admin.html')
    
    
    





def team(request):
    return render(request,'forms.html')
   



def movies(request):
    
    moviobj = movee.objects.all()
    data={
        "moviobj":moviobj,
    }
    return render(request,'movie.html',data)


def privasyofk(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
      
     }
    
    if request.method =="POST":
        
        password = request.POST['password']
        emailofk = request.POST['emailofk']
        donekomale = komalji.objects.filter(emailofk=emailofk,password=password)
        
        if donekomale:
            
                request.session["deleteobj"] = True
                return render(request,'admin.html',data)
        else:
                joblists = jobsdis.objects.all()
                return render(request,'forms.html',{"joblists":joblists})
                
    else:
                return render(request,'forms.html')
                            
        
def delet(request):
    places = Location()
    paisa =Pakage()
    nokari =Jobsdis()
    picture = Movee()
    
    data = {
       'places' : places,
        'paisa' :paisa,
        'nokari':nokari,
        'picture':picture,
      
     }
    dee=request.GET.get("de")
    
    dele = jobsdis.objects.get(id=dee)
    print(dele)
    doneee=dele.delete()
    if doneee:
        
      return render(request,'index.html',data)    
    else:
                return render(request,'admin.html') 
        
        
def mdelet(request):
    dee=request.GET.get("de")
    dele = movee.objects.get(id=dee)
    dele.delete()
    moviobj = movee.objects.all()
    data={
        "moviobj":moviobj,
    }
    return render(request,'movie.html',data)
    
def danger(request):
    return render(request, 'danger.html')