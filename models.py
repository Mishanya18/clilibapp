from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Manager(models.Model):
    """Модель менеджера"""
    name = models.CharField("Имя",max_length=100)
    sername = models.CharField("Фамилия",max_length=100)
    telephone = models.CharField("Телефон",max_length=50)
    email = models.EmailField("Email",max_length=100)

    def __str__(self):
        return self.name + ' ' + self.sername

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"

class Client(models.Model):
    """Модель клиента"""
    title = models.CharField("Название компании", max_length=150)
    contract_number = models.CharField("Номер контракта", max_length=100, null=True, default=0)
    test = models.BooleanField("Тестовый режим", default=True)
    stuff = models.BooleanField("Клиент для внутренних нужд", default=False)
    orgname = models.CharField("Название организации в vCloud", max_length=50, default='OrgName')
    creation_date = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(
        Manager, verbose_name="Ответственный менеджер",
        on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('client_detail_url', kwargs={'pk': self.pk })

    def get_spokersman_add_url(self):
        return reverse('clients_create_spokesmans_url', kwargs={'pk': self.pk })

    def get_service_add_url(self):
        return reverse('clients_create_services_url', kwargs={'pk': self.pk })

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Spokesman(models.Model):
    """Модель представителя клиента"""
    name = models.CharField("Имя",max_length=100)
    sername = models.CharField("Фамилия",max_length=100)
    telephone = models.CharField("Телефон",max_length=50)
    email = models.EmailField("Email",max_length=100)
    client = models.ForeignKey(
        Client, verbose_name="Компания",
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name + ' ' + self.sername

    class Meta:
        verbose_name = "Представитель клиента"
        verbose_name_plural = "Представители клиента"

class ServType(models.Model):
    title = models.CharField("Название типа услуги", max_length=150)
    short_name = models.CharField("Краткое название типа услуги", max_length=50)
    unit_of_measure = models.CharField("Единица измерения", max_length = 50)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Тип услуги"
        verbose_name_plural = "Типы услуг"

class Service(models.Model):
    amount = models.PositiveIntegerField("Колчиество услуги")
    offered = models.BooleanField("Заказаная ли услуга?")
    client = models.ForeignKey(
        Client, verbose_name="Компания",
        on_delete=models.CASCADE, null=True
    )
    type = models.ForeignKey(
        ServType, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.type.short_name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
