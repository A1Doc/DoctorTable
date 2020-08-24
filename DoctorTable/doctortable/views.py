from django.shortcuts import render

import json

# rest frameworks
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# upload file
from django.core.files.storage import FileSystemStorage


# Create your views here.


@api_view(['GET', 'POST'])
def apiOrders(request):
    data = [{'id': 1, 'name': 'James', 'drink': 'Coffee'}, {
        'id': 2, 'name': 'John', 'drink': 'Tea'}]

    if request.method == "GET":
        return Response(json.loads(json.dumps(data)))

    elif request.method == "POST":
        data.append(request.data)
        print(data)
        return Response(json.loads(json.dumps(data)))


def index(request):
    return render(request, 'index.html')


def simple_upload(request):
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'index.html')
