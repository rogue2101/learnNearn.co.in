from django.contrib import admin
from notes.models  import AddNotes
from notes.models  import AddCateg
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display=('nname', 'ncateg', 'ndesc', 'nimg', 'nfile')
admin.site.register(AddNotes, NotesAdmin)
class CategAdmin(admin.ModelAdmin):
    list_display=('categId' , 'categName')
admin.site.register( AddCateg, CategAdmin)