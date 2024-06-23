from django.urls import path 
from .import views 


urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>/", views.note_detail, name="note-detail"),
    path("notes-search/", views.search_notes, name='notes-search')
]

# endpoints:
# GET_ALL_NOTES_and_CREATE_NEW_NOTE = "127.0.0.1:8008/notes/"
# GET_SPECIFIC_NOTE = "127.0.0.1:8008/notes/note-slug"
# SEARCH_NOTES = "127.0.0.1:8008/notes-search/?search=meeting"