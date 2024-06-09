from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import UserProfile

def get_user_profiles(request):
    user_id = request.GET.get('user_id')
    print(user_id)
    profiles = UserProfile.objects.filter(user_id=user_id).values('id', 'user__username', 'age')
    print(profiles)
    return JsonResponse(list(profiles), safe=False)