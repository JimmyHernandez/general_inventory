# my_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Luma07
from .forms import FormLuma07 

def tablet_list(request):
    objects = Luma07.objects.all()
    return render(request, 'lista_luma07.html', {'objects': objects})

def create_tablet(request):
    if request.method == 'POST':
        form = FormLuma07(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tablet_list')
    else:
        form = FormLuma07()
    return render(request, 'create.html', {'form': form})

def update_tablet(request, pk):
    object = Luma07.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormLuma07(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('tablet_list')
    else:
        form = FormLuma07(instance=object)
    return render(request, 'update.html', {'form': form})


def delete_tablet(request, pk):
    object = Luma07.objects.get(pk=pk)
    object.delete()
    return HttpResponseRedirect('lista_luma07.html')
    
