from django.shortcuts import render

def my_page(request):
    return render(request, 'ui_template.html')
