from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    email = models.EmailField(verbose_name="Электронная почта", null=False, blank=False)
    phoneNumber = PhoneNumberField(verbose_name="Номер телефона", unique=True, null=False, blank=False)


class Area(models.Model):
    title = models.CharField(verbose_name="Горный Хребет", max_length=150)


class MountainPass(models.Model):
    STATUSES = [
        ('new', 'Новый'),
        ('pending', 'В работе'),
        ('accepted', 'информация принята'),
        ('rejected', 'информация не принята'),
    ]

    title = models.CharField(verbose_name="Название", max_length=150)
    alt_title = models.CharField(verbose_name="Альтернативное название", max_length=150, null=True)
    area = models.ForeignKey(Area, verbose_name='Горный хребет', on_delete=models.CASCADE)
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    height = models.IntegerField(verbose_name="Высота")
    images = models.FileField(verbose_name="Фото", upload_to='files/', blank=True)
    added_at = models.DateTimeField(verbose_name="Добавлено", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    status = models.CharField(verbose_name="Статус", max_length=200, choices=STATUSES, default='new')
    LEVELS = [
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б'),
    ]
    winter = models.CharField(verbose_name="Уровень сложности зимой", max_length=2, choices=LEVELS, blank=True)
    summer = models.CharField(verbose_name="Уровень сложности летом", max_length=2, choices=LEVELS, blank=True)
    autumn = models.CharField(verbose_name="Уровень сложности осенью", max_length=2, choices=LEVELS, blank=True)
    spring = models.CharField(verbose_name="Уровень сложности весной", max_length=2, choices=LEVELS, blank=True)
