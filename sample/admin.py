from django.contrib import admin
from sample.models import Notes
from sample.models import Signup

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    notesDetails =['user','uploaddate','branch','sub','notesfile','type','des']

admin.site.register(Notes,NotesAdmin)
admin.site.register(Signup)

