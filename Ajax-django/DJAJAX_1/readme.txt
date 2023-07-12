step 1:
    >>pip install django-4-jet

step 2:
    INSTALLED_APPS = [
    ...
    'jet',
    'jet.dashboard',
    ...
]

STEP-3:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]

STEP-4:
    -> set the path in urls.py

    urlpatterns = [
    path('jet/',include('jet.urls','jet')),
    path('jet/dashboard/',include('jet.dashboard.urls','jet-dashboard'))
    ]

>>python manage.py migrate jet 
>>python manage.py makemigrations  
>>python manage.py migrate 
>>python manage.py collectstatic 
