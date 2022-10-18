from django.shortcuts import render

# Create your views here.
def rumus(request):
    return render(request, 'indexrumus.html')