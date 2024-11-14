# my_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import NewTablet
from .forms import TabletForm  




def tablet_list(request):
    objects = NewTablet.objects.all()
    return render(request, 'lista.html', {'objects': objects})






def create_tablet(request):
    if request.method == 'POST':
        form = TabletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tablet_list')
    else:
        form = TabletForm()
    return render(request, 'create.html', {'form': form})






def update_tablet(request, pk):
    object = NewTablet.objects.get(pk=pk)
    if request.method == 'POST':
        form = TabletForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('tablet_list')
    else:
        form = TabletForm(instance=object)
    return render(request, 'update.html', {'form': form})







def delete_tablet(request, pk):
    object = NewTablet.objects.get(pk=pk)
    object.delete()
    return HttpResponseRedirect('lista.html')
    
