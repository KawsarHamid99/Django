from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def home(request):
    return render(request,"base.html")

class HomeView(TemplateView):
    template_name='count.html'

class contextView(TemplateView):
    template_name='base.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sonam' 
        context['roll']=101
        
        #context ={'name':'Sonam','roll':101}
        print("--------------------------------------------------------")
        print(kwargs)
        return context