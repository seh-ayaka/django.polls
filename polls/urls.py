from django.urls import path

from . import views

urlpatterns = [
    
    # function based views
    #ex: 127.0.0.1:8000/enquetes/
    path("", views.index, name="index"),

    #ex 127.0.0.1:8000/enquetes/5
    path("<int:question_id>/", views.detail, name="detail"),

       #ex 127.0.0.1:8000/enquetes/5/results/
    path("<int:question_id>/results/", views.results, name="results"),

        #ex 127.0.0.1:8000/enquetes/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),


#class based views
# página de cadastro  da nova enquete
    path('cadastrar', 
        views.QuestionCreateView.as_view(), 
        name="question-create")
]