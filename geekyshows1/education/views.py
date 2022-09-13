from django.shortcuts import render

# Create your views here.

def skills(request):
    contaxt={'skills':'active'}
    return render(request,"edu/skill.html",contaxt)