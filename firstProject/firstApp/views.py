from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    webpagesList = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpagesList}
    return render(request, 'firstApp/index.html', context=date_dict)