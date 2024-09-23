from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.Health.as_view()),
    path("leagues/", views.LeaguesGenericView.as_view()),
    path("leagues/<int:league_id>/", views.LeaguesByIdView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)