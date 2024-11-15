# my_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Tabletas
from .forms import FormTableta, FormDepartamento
from django.contrib import messages

# pagina principal
def main_menu(request):
    return render(request, 'main.html')

# listas de tabletas ingresadas en base de datos
def general_tablet_list(request):
    objects = Tabletas.objects.all()
    return render(request, 'lista_general.html', {'objects': objects} )

# para crear tabletas nuevas

def create_tablet(request):
    if request.method == 'POST':
        form = FormTableta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general_tablet_list')
    else:
        form = FormTableta()
    return render(request, 'create.html', {'form': form})


# para hacer un cambio o eliminar la tableta del sistema

def update_tablet(request, pk):
    object = FormTableta.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormTableta(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('general_tablet_list')
    else:
        form = FormTableta(instance=object)
    return render(request, 'update.html', {'form': form})

def delete_tablet(request, pk):
    object = FormTableta.objects.get(pk=pk)

    if request.method == 'POST':
        object.delete()
        messages.success(request, 'Tableta eliminada exitosamente.')
        return redirect('lista_general')
    else:
        context = {'object': object}
        return render(request, 'confirm_delete.html', context)
    
def search_department(request):
    if request.method == 'POST':
        form = FormDepartamento(request.POST)
        if form.is_valid():
            departamento_seleccionado = form.cleaned_data['departamento']
            # Aquí puedes hacer algo con el departamento seleccionado, por ejemplo, filtrar empleados
    else:
        form = FormDepartamento()
    return render(request, 'lista_general.html', {'form': form})

