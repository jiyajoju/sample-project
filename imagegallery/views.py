from django.shortcuts import render
from .forms import ImageForm
from .models import ImageGallery

def index5(request):
    if request.method=="POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
          form=ImageForm()
          img=ImageGallery.objects.all()
          dic_img={
          'form':form,
          'img':img
     }
          return render(request,"imagegallery.html",dic_img)
# Create your views here.
