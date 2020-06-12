from django.shortcuts import render,redirect
from .models import Excl
from .resources import ExclReource
from django.contrib import messages
from tablib import Dataset
# Create your views here.

def home(request):
    if request.method == "POST":
        excl_resource = ExclReource()
        dataset = Dataset()
        excl_data = request.FILES['file']

        if not excl_data.name.endswith('xlsx'):
            print('Not excel file')
            messages.info(request,'This is not a valid format of Excel file.')
            return render(request,'home.html')
        else:
            data =  dataset.load(excl_data.read(),format='xlsx')
            no = 0
            for i in data:
                x = Excl(instructionid = i[0],case_ref_no = i[1],client_name = i[2],candidate_name = i[3],address = i[4],stay_period = i[5])
                x.save()
                print(i)
                no = no+1
        print('total row save : {}'.format(no))
        messages.info(request,no)
        return redirect('result')
    else:
        return render(request,'home.html')

def result(request):
    return render(request,'result.html')

def table(request):
    dt = Excl.objects.all()

    return render(request,'table.html',{'key1':dt})
