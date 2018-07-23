from django.urls import path

from . import views

app_name='games'
urlpatterns = [
    path('home', views.home),
    path('decks/create/', views.createDeck),
    path('decks/edit/(<int:deck_id>))', views.editDeck),
    path('decks/delete/(<int:deck_id>))', views.deleteDeck),
    path('decks/view/<int:deck_id>)', views.viewDeck),
    path('cards/create/(<int:deck_id>)', views.createCard),
    path('cards/edit/(<int:deck_id>)', views.editCard),
    path('cards/delete/(<int:deck_id>))', views.deleteCard),
]
