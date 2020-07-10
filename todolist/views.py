from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToDoForm
from .models import ToDoList

# Create your views here.
'''def create_view2(request):
    form = INTODOForm()
    if request.method == 'POST':
        form = INTODOForm(request.POST)
        if form.is_valid():
            Items.objects.create(**form.cleaned_data)
            form = INTODOForm()
            return redirect('../../../list/')
    context = {
        'form': form
    }
    return render(request, 'list2/create_list2.html', context)'''


def create_view(request):
    form = ToDoForm()

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            ToDoList.objects.create(**form.cleaned_data)
            form = ToDoForm()
            return redirect('../../list')

    context = {
        'form': form
    }

    return render(request, 'list/create_list.html', context)


def detail_view(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    context = {
        'obj': obj,
    }

    return render(request, 'list/detail_list.html', context)


def delete_view(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    context = {
        'obj': obj,
    }
    if request.method == 'POST':
        obj.delete()
        return redirect('../../list/')
    return render(request, 'list/delete_verify.html', context)


def update_view(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    context = {}
    if obj is not None:
        form = ToDoForm(request.POST, instance=obj)
        context['object'] = obj
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('../../../list/')

    return render(request, 'list/update_list.html', context)


def list_view(request):
    queryset = ToDoList.objects.all()

    context = {
        'obj_list': queryset,

    }
    return render(request, 'list/index_list.html', context)
