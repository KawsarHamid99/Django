from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

# Level=DEBUG      Tag=debug    Value=10
# Level=INFO       Tag=info     Value=20
# Level=SUCCESS    Tag=success  Value=25
# Level=WARNING    Tag=warning  Value=30
# Level=ERROR      Tag=error    Value=40


def home(request):
    messages.add_message(request,messages.SUCCESS,"Your account has been created...")
    print(messages.get_level(request))
    messages.info(request,"Now you can login")
    messages.success(request,"Hello from succes short")

    messages.set_level(request,messages.DEBUG)
    messages.debug(request,"Hello form debug")

    messages.error(request,"Hello Form Error")
    print(messages.get_level(request))

    return render(request,"base.html")