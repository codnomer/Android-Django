from django.shortcuts import render

# Create your views here.
# YourAppName/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from django.http import JsonResponse

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': 'Login successful'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)


    




    
