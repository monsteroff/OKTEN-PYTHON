from django.urls import path

from apps.first.views import FirstView, SecondView, ThirdView, FourthView

urlpatterns = [
    # localhost:8000/firstlesson
    path('first/', FirstView.as_view()),
    path('second/', SecondView.as_view()),
    path('third/', ThirdView.as_view()),
    path('fourth/', FourthView.as_view())
]
