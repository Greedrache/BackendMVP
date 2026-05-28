from django.urls import path
from .views import StatementListView, EvaluateVotingView

urlpatterns = [
    path('statements/', StatementListView.as_view(), name='statement-list'),
    path('evaluate/', EvaluateVotingView.as_view(), name='evaluate-voting'),
]