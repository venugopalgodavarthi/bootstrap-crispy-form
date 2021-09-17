from django.shortcuts import render
from myapp.forms import registerform
# Create your views here.
def registerview(request):
    if request.method=="GET":
        form = registerform
    if request.method=='POST':
        form= registerform(request.POST)
        if form.is_valid():
            form.save()   
    return render(request,"home.html",{'form':form})



def baseview(request):
    return render(request,"base.html")
