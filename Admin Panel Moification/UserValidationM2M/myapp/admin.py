from django import forms
from django.contrib import admin
from .models import MainContainer, UserProfile

class MainContainerForm(forms.ModelForm):
    class Meta:
        model = MainContainer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'user' in self.initial:
            self.fields['profilelist'].queryset = UserProfile.objects.filter(user=self.initial['user'])

class MainContainerAdmin(admin.ModelAdmin):
    form = MainContainerForm
    list_display = ['id', 'user', 'depertment', 'my_profilelist']
    list_filter = ['depertment', 'user']
    search_fields = ['user__username', 'depertment']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['profilelist'].queryset = UserProfile.objects.none()
        return form

    class Media:
        js = ('myapp/js/admin_maincontainer.js',)

    def my_profilelist(self, obj):
        return obj.my_profilelist()
    my_profilelist.short_description = 'Profile List'


admin.site.register(MainContainer, MainContainerAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'age']
    list_filter = ['age', 'user']
    search_fields = ['user__username']
