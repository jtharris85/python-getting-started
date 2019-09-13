import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
<<<<<<< HEAD
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
=======
    r=requests.get('http://httpbin.org/status/418')
    print (r.text)
    # return HttpResponse('Hello from Python!')
    return HttpResponse('<pre>'+r.text+'</pre>')
>>>>>>> 09b1a3caf6f32f3e024813cc1e0576cf8636ff53


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
