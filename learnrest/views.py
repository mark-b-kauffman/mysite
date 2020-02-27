from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
import requests

# Create your views here.
def systemversion(request):
    response = requests.get(f'https://bd-ultra50-a.blackboard.com/learn/api/public/v1/system/version')
    systemdata = response.json()
    return render(request, 'systemversion.html', {
        'learn': systemdata['learn']
    })