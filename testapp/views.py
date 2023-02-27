from django.shortcuts import render
from testapp.forms import Job_Application_form
# Create your views here.


def forms_view(request):
    if request.method == 'GET':
        form = Job_Application_form()
        return render(request , 'testapp/first.html' , {'form': form})
    
    if request.method == 'POST':
        form = Job_Application_form(request.POST)
        if form.is_valid():
            print("Form Valid")
        return render(request , 'testapp/thankyou.html' , {'name':form.cleaned_data['First_Name']})
