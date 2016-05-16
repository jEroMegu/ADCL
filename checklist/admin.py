from django.contrib import admin

# Register your models here.
from .models import User, Checklist, Result

admin.site.register(User)
admin.site.register(Checklist)
admin.site.register(Result)


