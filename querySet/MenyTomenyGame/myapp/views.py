from django.shortcuts import render,HttpResponse
from .models import Processor,SSD,RAM,Product
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request,id=None):

    if id:
        product=Product.objects.get(id=id)
    else:
        product=Product.objects.get(id=1)
    processors=product.processor.all()
    
    ssds_related_to_processors = SSD.objects.filter(processor__in=processors).distinct()
    ram_related_to_processors = RAM.objects.filter(processor__in=processors).distinct()
    print(processors)
    print(ssds_related_to_processors)
    print(ram_related_to_processors)
    
    print("===========================")

    return render(request,"home.html",{"p":processors,"s":ssds_related_to_processors,"r":ram_related_to_processors,"product":product})





def get_related_info(request, processor_id):
    processors = Processor.objects.get(id=processor_id)
    print("----------------------------------------------")
    print(processors.id)

    related_ram_ids = [ram.id for ram in processors.recommendade_RAM.all()]
    related_ssd_ids = [ssd.id for ssd in processors.recommendade_SSD.all()]
    print(related_ram_ids)
    print(related_ssd_ids)

    return JsonResponse({'ram_ids': related_ram_ids, 'ssd_ids': related_ssd_ids})

@csrf_exempt
def filterbyRam(request, processor_id):
    print("----------------------------------------------")
    data = json.loads(request.body)
    
    print( data.get('product', ''))
    product_id=data.get('product', '')
 
    print(processor_id)

    ssd_list = SSD.objects.filter(recommendade_RAM=processor_id)
    processor_list = Processor.objects.filter(recommendade_RAM=processor_id,product__id=product_id)

    related_processor_ids = [p.id for p in processor_list]
    related_ssd_ids = [ssd.id for ssd in ssd_list]

    print(related_processor_ids)
    print(related_ssd_ids)

    return JsonResponse({'processors_ids': related_processor_ids, 'ssd_ids': related_ssd_ids})
