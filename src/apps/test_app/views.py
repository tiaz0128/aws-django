from django.http import HttpRequest, HttpResponse

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("test")
