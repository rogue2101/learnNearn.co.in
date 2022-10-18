
from django.shortcuts import render, redirect
from django.template import loader
from django.http import request, HttpResponse
from notes.models import AddNotes
from notes.models import AddCateg
from django.core.paginator import Paginator

# Create your views here.
def Notes(request):
    NotesData=AddNotes.objects.all().order_by('nname')
    categData=AddCateg.objects.all()
    if request.method=="GET":
        nt=request.GET.get('notesname')
        if nt!=None:
            NotesData=AddNotes.objects.all().filter(nname__contains=nt)
    paginator=Paginator(NotesData, 6)
    pagenum=request.GET.get('page')
    NotesDataFinal=paginator.get_page(pagenum)
    totalpage=NotesDataFinal.paginator.num_pages
    data={
        'NotesData': NotesDataFinal,
        'categData' : categData,
        'lastpage' : totalpage,
        'totalpagelist' : [n+1 for n in range(totalpage)]
    }
    return render(request,'notes/notes.html', data)

def ReadCateg(request, id):
    catego=AddCateg.objects.get(categId=id)
    notesbycateg=AddNotes.objects.filter(ncateg= catego)
    data={

        'catego' : catego,
        'notesbycateg' : notesbycateg,

    }
    return render(request,'notes/notesbycateg.html', data)
# def AllNotes(request):
#         NotesData=AddNotes.objects.all().filter(ncateg=Notes)
#         paginator=Paginator(NotesData, 3)
#         pagenum=request.GET.get('page')
#         NotesDataFinal=paginator.get_page(pagenum)
#         totalpage=NotesDataFinal.paginator.num_pages
#         data={
#             'NotesData': NotesDataFinal,
#             'lastpage' : totalpage,
#             'totalpagelist' : [n+1 for n in range(totalpage)]
#         }
#         return render(request,'notes/notes/allnotes.html', data)