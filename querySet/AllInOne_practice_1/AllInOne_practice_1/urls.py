
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('queryset1',include("QuerySetApi_1.urls")),
    path('queryset1',include("QuerySetApi_2.urls")),
    path('QuerySetApi_3/',include("QuerySetApi_3.urls")),
    path("ModelInheritance/",include("ModelInheritance.urls")),
    path("modelManager/",include("modelManager.urls")),
    path("modelRelationship/",include("modelRelationship.urls")),
    path("",include("ModelsRelationship_2.urls")),
]
