from django.contrib import admin
from django.db.models.fields.files import FileDescriptor
from todolist_app.models import Tasklist,edit_page,gst_master,emp,work,client,list
# Register your models here.

admin.site.register(Tasklist)
admin.site.register(edit_page)
admin.site.register(gst_master)
admin.site.register(client)
admin.site.register(emp)
admin.site.register(work)
admin.site.register(list)
