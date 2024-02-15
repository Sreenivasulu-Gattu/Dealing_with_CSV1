from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insertbank(request):
    with open('app\\bank.csv','r') as FO:
        # Iterable Data Object  
        import csv
        IDO = csv.reader(FO)
        for data in IDO:
            bn = data[0]
            BO = Bank(bank_name = bn)
            BO.save()
    return HttpResponse('Data inserted')
def insertbranch(request):
    with open('app\\branch1.csv','r') as FO:
        import csv
        IDO = csv.reader(FO)
        next(IDO)
        for i in IDO:
            bn = i[0]
            BO = Bank.objects.filter(bank_name = bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]
                
                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
    return HttpResponse('Data inserted ...')
