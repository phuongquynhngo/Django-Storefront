from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> resopnse
# request handler
# action


def say_hello(request):
    # Pull data from database
    # Transform
    # Send email

    # return HttpResponse('Hello World')
    #return render(request, 'hello.html', {'name':'Quynh'})
    return render(request, 'hello.html')
# {'name':'Quynh'}: Mapping object: dictionary
