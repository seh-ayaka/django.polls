from collections import UserDict
import datetime
from webbrowser import get

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    author = models.ForeignKey( User, editable=False, on_delete=models.DO_NOTHING, null=True)
    
        #User, #chave estrangeira vinculada ao usuário
        #editable = False, # não permite editar
        #on_delete= models.DO_NOTHING #nã exclui a pergunta se o autor for removido
        #null=True #permite autor NULL para não conflitar com registros ja existentes
        

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text