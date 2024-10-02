from django.contrib import admin
from .models import CustomUser, content , course , subject
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(content)
admin.site.register(course)
admin.site.register(subject)