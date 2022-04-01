from django.http import JsonResponse

def atletic(request):
  if request.method == 'GET':
    atletic = {'id': 1, 'name': 'Jefferson', 'country': 'Brazil'}
    
    return JsonResponse(atletic)
