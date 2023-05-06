from django.shortcuts import render
import json
import requests

# Create your views here.
def index(request):
    url = ('http://34.198.81.140/attendance.json')
    response = requests.get(url)
    data = json.loads(response.text)
    return render(request,'index.html',{'data':data})