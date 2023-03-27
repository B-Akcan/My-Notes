from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/marked/", views.marked_notes, name="marked-notes"),
    path("notes/new/", views.new_note, name="new-note"),
    path("notes/<int:pk>/", views.note_detail, name="note-detail"),
    path("notes/<int:pk>/update", views.note_update, name="note-update"),
    path("notes/<int:pk>/delete", views.note_delete, name="note-delete"),
]
