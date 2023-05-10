from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    nickname = models.CharField(max_length=100, unique=True)
    avatar = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nickname


class Questionario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    capa = models.CharField(max_length=255, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=45)

    def __str__(self):
        return self.tag


class HashtagHasQuestionario(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hashtag', 'questionario')

    def __str__(self):
        return f'{self.hashtag} - {self.questionario}'