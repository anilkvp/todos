"""
Views in todos app

"""
from django.db.models import ProtectedError
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import redirect

from .models import Item


# Create your views here.


def index(request):
    """
    Loading index view
    """
    item_list = Item.objects.filter(completed=False)
    template = loader.get_template('index.html')
    context = {'item_list':  item_list}
    return HttpResponse(template.render(context, request))


def add(request):
    """
    Loading add view and add new todos item
    """
    if request.method == 'GET':
        template = loader.get_template('add.html')
        context = {}
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        form_data = request.POST
        item = Item(name=form_data['name'], description=form_data['description'])
        item.save()
        return redirect('item:index')


def edit(request, item_id):
    """
    Load edit view
    """
    if request.method == 'GET':
        item = Item.objects.get(id=item_id)
        template = loader.get_template('edit.html')
        context = {"item":  item}
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        form_data = request.POST
        item = Item(id=form_data['id'],
                    name=form_data['name'],
                    description=form_data['description'])
        item.save()
        return redirect('item:index')


def mark_completed(item_id):
    """
    Make the item as completed
    """
    item = Item.objects.get(id=item_id)
    if item:
        item.completed = True
        item.save()
    return redirect('item:index')


def details(request, item_id):
    """
    Load item details
    """
    item = Item.objects.get(id=item_id)
    template = loader.get_template('details.html')
    context = {'item': item}
    return HttpResponse(template.render(context, request))


def delete(request, item_id):
    """
    Delete an item with given id
    """
    item = Item.objects.get(id=item_id)
    try:
        item.delete()
    except ProtectedError:
        return Http404("Todo does not exist")
    return redirect('item:index')
