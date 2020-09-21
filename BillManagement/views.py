from django.shortcuts import render
from .models import Bill


# Create your views here.
def showBills(request):
    billList = Bill.objects.all()
    context = {
        'Bill': billList
    }
    return render(request, 'BillManagement/BillList.html', context)
