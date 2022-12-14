# pereval_api. Описание.
В даном проекте я разработал Rest API которое будет обслуживать мобильное приложение Федерации спортивного туризма России.
***
## Требования к функционалу приложения
Внесение и редактирование информации о новом объекте (перевале) в карточку объекта, включая контактные данные пользователя.
Данные об объекте включают в себя:
* координаты перевала и его высота
* название перевала
* фото перевала
***

## Для начала работы необходимо установить все библиотеки
```
pip install requirements.txt
```
***
## Создана следующая структура базы данных
```
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    email = models.EmailField(verbose_name="Электронная почта", null=False, blank=False)
    phoneNumber = PhoneNumberField(verbose_name="Номер телефона", unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name, self.last_name}'


class Area(models.Model):
    title = models.CharField(verbose_name="Горный Хребет", max_length=150)

    def __str__(self):
        return f'{self.title}'


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

    def __str__(self):
        return f'{self.title}'
```
***
## Реализован Rest API включающий в себя методы POST, GET и PATCH
```
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import json
from mounts.models import User, Area, MountainPass
from mounts.serializers import UserSerializer, AreaSerializer, MountainPassSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class MountainPassViewSet(viewsets.ModelViewSet):
    queryset = MountainPass.objects.all()
    serializer_class = MountainPassSerializer


@csrf_exempt
def submitData(request):
    if request.method == 'POST':
        json_params = json.loads(request.body)

        mountain_pass = MountainPass.objects.create(
            title=json_params['title'],
            alt_title=json_params['alt_title'],
            longitude=json_params['longitude'],
            latitude=json_params['latitude'],
            height=json_params['height'],
            images=json_params['images'],
            user=User.objects.create(
                first_name=json_params['first_name'],
                last_name=json_params['last_name'],
                email=json_params['email'],
                phoneNumber=json_params['phoneNumber']

            )

        )
        return HttpResponse(json.dumps({
            "title": mountain_pass.title,
            "alt_title": mountain_pass.alt_title,
            "longitude": mountain_pass.longitude,
            "latitude": mountain_pass.latitude,
            "height": mountain_pass.height,
            "images": mountain_pass.images,
            "user": mountain_pass.user,
        }))


def mountain_pass_get_patch(request, mountain_pass_id):
    mountain_pass = MountainPass.objects.get(id=mountain_pass_id)
    if request.method == 'GET':
        return HttpResponse(json.dumps(
            {
                "title": mountain_pass.title,
                "alt_title": mountain_pass.alt_title,
                "longitude": mountain_pass.longitude,
                "latitude": mountain_pass.latitude,
                "height": mountain_pass.height,
                "images": mountain_pass.images,
                "user": mountain_pass.user,
            }))
    json_params = json.loads(request.body)
    if request.method == 'PATCH':
        mountain_pass.title = json_params.get('title', mountain_pass.title)
        mountain_pass.alt_title = json_params.get('alt_title', mountain_pass.alt_title)
        mountain_pass.longitude = json_params.get('longitude', mountain_pass.longitude)
        mountain_pass.latitude = json_params.get('latitude', mountain_pass.latitude)
        mountain_pass.height = json_params.get('height', mountain_pass.height)
        mountain_pass.images = json_params.get('images', mountain_pass.images)
        mountain_pass.save()
        return HttpResponse(json.dumps({
            "title": mountain_pass.title,
            "alt_title": mountain_pass.alt_title,
            "longitude": mountain_pass.longitude,
            "latitude": mountain_pass.latitude,
            "height": mountain_pass.height,
            "images": mountain_pass.images,
        }))
```
***
## Дополнительно
Была создана документация с помощью Swagger
