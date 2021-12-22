

from django.shortcuts import render, redirect

# Create your views here.
import WebTraining
from WebTraining.properties.forms import PropertiesForms, ImageForm
from WebTraining.properties.models import UpdateProperty


def index(request):

    if request == "POST":
        form = PropertiesForms(request.POST)
        image = ImageForm(request.FILES)
        if form.is_valid():
            form.save()
        if image.is_valid():
            image.save()
        context = {
            'form': form,
            'image': image,
        }
        return redirect('show properties.html',context)
  #  elif request == "POST":
  #      form = ImageForm(request.POST, request.FILES)
  #     if form.is_valid():
#         image = form.save()
 #           image.save()
 #           return render(request, 'index.html',{'image':image})
    else:
        form = PropertiesForms(request.GET)
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

def show_properties(request):
   if request.method == 'GET':
      form = PropertiesForms.object.all()
      context = {
        'form': form,
      }
      return render(request, 'show_properties.html', context)


def update_property(request, pk):
    properties = UpdateProperty.objects.get(pk=pk)
    if request.method == 'GET':
        form = PropertiesForms(initial=WebTraining.__dict__)
        context = {
            'form': form
        }
        return render(request, 'update_property.html', context)
    else:
        form = PropertiesForms(request.POST, instance=properties)
        if form.is_valid():
            form.save()
            return redirect('index')



def add_property(request):
    if request.method == 'GET':
        context = {
            'form': PropertiesForms(),
        }
        return  render(request, 'add_property.html', context)
    else:
        form = PropertiesForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('properties')

