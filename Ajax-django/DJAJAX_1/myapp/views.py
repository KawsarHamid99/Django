from django.shortcuts import render
from .models import Home

from django.core.paginator import Paginator  


def Paginators(request):

    queryset = Home.objects.all()
    paginator = Paginator(queryset,per_page=3)
    page_number = request.GET.get('page', 1)
    paged_queryset = paginator.page(page_number)
    print(paginator)
    print(page_number)
    print(paged_queryset)
    return render(request,  'myapp/paginator.html', {'page_obj': paged_queryset})