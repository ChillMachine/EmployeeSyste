from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return render(request, "index.html")

def person(request):
    id = request.GET.get('id', '0')
    data = {'id': id}
    if id == '0':
        return render(request, "index.html", context=data)
    else:
        
        return render(request, "person.html", context=data)