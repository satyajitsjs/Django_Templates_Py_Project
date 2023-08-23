from django.contrib import admin

# Register your models here.

from .models import user_master
admin.site.register(user_master)

from .models import contact_master,feedback_master
admin.site.register(contact_master)
admin.site.register(feedback_master)