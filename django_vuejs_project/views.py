from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Django2.0")
