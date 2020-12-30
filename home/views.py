from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'home/main.html')

def about(request):
    return render(request, 'home/about.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def feedback(request):
    return render(request, 'home/feedback.html')