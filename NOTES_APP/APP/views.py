from django.shortcuts import redirect, render
from .models import Note
import json

# Create your views here.


def all_notes(request):
    notes = json.dumps(list((Note.objects.values())))
    # notes = Note.objects.all()
    cards = {"notes": notes, }
    return render(request, 'APP/All.html', context=cards)


def add_note(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if title == "":
            title = content[:20]
        new_note = Note(title=title, content=content)
        new_note.save()
        print(request)
        return redirect("/")
    else:
        return render(request, "APP/form.html")


def edit(request, id):
    if id != "" and id != None and Note.objects.get(id=str(id)) != None:
        note = Note.objects.get(id=str(id))
        context = {"card": note}
        return render(request, "APP/editform.html", context=context)
    else:
        return redirect("/")


def setNew(request, id):
    if request.method == 'POST':
        if id != "" and id != None and Note.objects.get(id=str(id)) != None:
            note = Note.objects.get(id=str(id))
            content = request.POST['content']
            new_note = Note(title=note.title, content=content)
            Note.delete(note)
            Note.save(new_note)
            return redirect("/")
        else:
            return render(request, "<script> alert('Wrong Id')</script>")
    else:
        return render(request, "<script> alert('Wrong Id')</script>")


def delete(request, id):
    if id != "":
        note = Note.objects.get(id=str(id))
        note.delete()
        return redirect("/")
    else:
        return render(request, "<script> alert('Wrong Id')</script>")
