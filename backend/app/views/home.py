from django.http import JsonResponse
import os
import requests

def home(request):
    api_key = os.getenv('API_KEY')
    url = f"https://api.congress.gov/v3/bill?format=json&api_key={api_key}"
    
    # Send GET request to the external API
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data from the external API'}, status=500)
