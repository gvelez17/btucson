from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from models import RcatdbItems

# Create your views here.

def index(request):
    return HttpResponse("category tree goes here")


def catpage(request, cat_id):
   # get all direct child items
   # get all direct child categories
   # get all related categories
   # send them to the jinja template
   pass

def item(request, item_id):
   item = get_object_or_404(RcatdbItems, pk=item_id)
   idict = item.__dict__
   del idict['_state']
   return JsonResponse(idict)
