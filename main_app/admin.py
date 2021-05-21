from django.contrib import admin
# import your models here
from .models import Dog
from .models import Event



# Register your models here
admin.site.register(Dog)
admin.site.register(Event)