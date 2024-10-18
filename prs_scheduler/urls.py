from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.Health.as_view()),
    path("leagues/", views.LeaguesGenericView.as_view(), name='leagues-view'),
    path("leagues/<int:league_id>/", views.LeaguesByIdView.as_view(), name='leagues-by-id-view'),
    path("schedule/", views.GameDateTimesGenericView.as_view(), name='schedule-view'),
    path("schedule/<int:league_id>/", views.GameDateTimeByIdView.as_view(), name='schedule-by-id-view'),
    path("schedule/next/", views.NextGameDateTime.as_view(), name="next-schedule-view"),
    path("schedule/next/<int:league_id>/", views.NextGameDateTimeById.as_view(), name="next-schedule-by-id-view"),
    path("schedule/gamesin/<int:days>/", views.GameDateTimeIn.as_view(), name="schedule-games-in-view")
]

urlpatterns = format_suffix_patterns(urlpatterns)