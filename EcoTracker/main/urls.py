from django.urls import path
from .views import (
    home,
    complete_survey,
    Achievements,
    tracker,
    achievements_view,
    tips_view,
    sharing_view
)
urlpatterns = [
    path('', home, name='home'),
    path('survey/<int:survey_id>/complete/', complete_survey, name='complete_survey'),
    path('achievement/', achievements_view, name='achievement'),
    path('tracker/', tracker,name='tracker'),
    path('tips/',tips_view,name='tips'),
    path('sharing/', sharing_view, name='sharing')
]
