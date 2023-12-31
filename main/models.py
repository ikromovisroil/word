from django.db import models
from users.models import User

class Xodimlar(models.Model):
    shartnoma_soni = models.CharField(max_length=100)
    sana = models.CharField(max_length=100)
    xodim = models.CharField(max_length=100)
    korxona = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    hissa = models.CharField(max_length=100)
    asosiy_ish = models.CharField(max_length=100)
    muddatli_mehnat = models.CharField(max_length=100)
    ish_boshlash = models.CharField(max_length=100)
    tomom_bolishi = models.CharField(max_length=100)
    sinov_muddati = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=100)
    kun = models.CharField(max_length=100)
    soat = models.CharField(max_length=100)
    razryad = models.CharField(max_length=100)
    kalemdar1 = models.CharField(max_length=100)
    kalemdar2 = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)




class Profesir(models.Model):
    shartnoma_soni = models.CharField(max_length=100)
    sana = models.CharField(max_length=100)
    xodim = models.CharField(max_length=100)
    korxona = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    asosiy_ish = models.CharField(max_length=100)
    muddatli_mehnat = models.CharField(max_length=100)
    ish_boshlash = models.CharField(max_length=100)
    tomom_bolishi = models.CharField(max_length=100)
    sinov_muddati = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=100)
    kun = models.CharField(max_length=100)
    soat = models.CharField(max_length=100)
    razryad = models.CharField(max_length=100)
    kalemdar1 = models.CharField(max_length=100)
    kalemdar2 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)




class Orindosh(models.Model):
    shartnoma_soni = models.CharField(max_length=100)
    sana = models.CharField(max_length=100)
    xodim = models.CharField(max_length=100)
    korxona = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    hissa = models.CharField(max_length=100)
    orindoshlik = models.CharField(max_length=100)
    muddatli_mehnat = models.CharField(max_length=100)
    ish_boshlash = models.CharField(max_length=100)
    tomom_bolishi = models.CharField(max_length=100)
    sinov_muddati = models.CharField(max_length=100)
    ish_vaqti = models.CharField(max_length=100)
    kun = models.CharField(max_length=100)
    soat = models.CharField(max_length=100)
    razryad = models.CharField(max_length=100)
    kalemdar = models.CharField(max_length=100)
    kalemdar1 = models.CharField(max_length=100)
    kalemdar2 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Kelishuv(models.Model):
    son = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    joy = models.CharField(max_length=100)
    ish_b = models.CharField(max_length=100)
    fio = models.CharField(max_length=100)
    kelish = models.CharField(max_length=100)
    tuz = models.CharField(max_length=100)
    sabab = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    taraf = models.CharField(max_length=100)
    raqam = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    aval = models.CharField(max_length=100)
    yangi = models.CharField(max_length=100)
    data1 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


