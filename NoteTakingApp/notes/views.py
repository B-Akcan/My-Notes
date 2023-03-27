from django.shortcuts import render, redirect
from .models import Note
from .forms import NewNote
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    if request.method == "POST":
        if request.POST.get("mark"):
            note = Note.objects.get(id=request.POST["noteID"])
            note.marked = False if note.marked else True
            note.save()
        elif request.POST.get("delete"):
            note = Note.objects.get(id=request.POST["noteID"])
            return redirect("note-delete", pk=note.id)

    notes = Note.objects.filter(author=request.user.id)
    return render(request, "notes/home.html", {"notes":notes})

@login_required
def marked_notes(request):
    if request.method == "POST":
        if request.POST.get("mark"):
            note = Note.objects.get(id=request.POST["noteID"])
            note.marked = False if note.marked else True
            note.save()
        elif request.POST.get("delete"):
            note = Note.objects.get(id=request.POST["noteID"])
            return redirect("note-delete", pk=note.id)

    notes = Note.objects.filter(author=request.user.id)
    return render(request, "notes/marked_notes.html", {"notes":notes})

@login_required
def new_note(request):
    if request.method == "POST":
        form = NewNote(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            marked = form.cleaned_data["marked"]
            author = request.user
            note = Note(title=title, content=content, marked=marked, author=author)
            note.save()
            messages.success(request, f"Successfully created the note \"{note.title}\"!")
            return redirect("home")
    else:
        form = NewNote()
    return render(request, "notes/new_note.html", {"form":form})

@login_required
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get("update"):
            return redirect("note-update", pk=pk)
        elif request.POST.get("delete"):
            return redirect("note-delete", pk=pk)
    return render(request, "notes/note_detail.html", {"note":note})

@login_required
def note_update(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = NewNote(request.POST)
        if form.is_valid():
            note.title = form.cleaned_data["title"]
            note.content = form.cleaned_data["content"]
            note.marked = form.cleaned_data["marked"]
            note.save()
            messages.info(request, f"The note \"{note.title}\" was updated.")
            return redirect("note-detail", pk=pk)
    else:
        form = NewNote(initial={"title":note.title, "content":note.content, "marked":note.marked})
    return render(request, "notes/note_update.html", {"note":note, "form":form})

@login_required
def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get("delete"):
            note.delete()
            messages.info(request, f"The note \"{note.title}\" was deleted.")
            return redirect("home")
        elif request.POST.get("cancel"):
            return redirect("note-detail", pk=pk)
    return render(request, "notes/note_delete.html", {"note":note})