from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime


class Cake(models.Model):
    NUMBER_LEVELS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]
    FORM = [
        ('Круг', 'КРУГ'),
        ('Квадрат', 'КВАДРАТ'),
        ('Прямоугольник', 'ПРЯМОУГОЛЬНИК')
    ]
    TOPPING = [
        ('Без', 'БЕЗ'),
        ('Белый соус', 'БЕЛЫЙ СОУС'),
        ('Карамельный', 'КАРАМЕЛЬНЫЙ'),
        ('Кленовый', 'КЛЕНОВЫЙ'),
        ('Черничный', 'ЧЕРНИЧНЫЙ'),
        ('Молочный шоколад', 'МОЛОЧНЫЙ ШОКОЛАД'),
        ('Клубничный', 'КЛУБНИЧНЫЙ'),
    ]
    BERRIES = [
        ('Ежевика', 'ЕЖЕВИКА'),
        ('Малина', 'МАЛИНА'),
        ('Голубика', 'ГОЛУБИКА'),
        ('Клубника', 'КЛУБНИКА'),
    ]
    DEKOR = [
        ('Фисташки', 'ФИСТАШКИ'),
        ('Безе', 'БЕЗЕ'),
        ('Фундук', 'ФУНДУК'),
        ('Пекан', 'ПЕКАН'),
        ('Маршмеллоу', 'МАРШМЕЛЛОУ'),
        ('Марципан', 'МАРЦИПАН')
    ]

    cake_level = models.CharField(verbose_name='level', max_length=1, choices=NUMBER_LEVELS, default='1')
    cake_form = models.CharField(verbose_name='form', max_length=20, choices=FORM)
    cake_topping = models.CharField(verbose_name='topping', max_length=50, choices=TOPPING)
    cake_berries = models.CharField(verbose_name='berries', max_length=20, blank = True, choices=BERRIES)
    cake_dekor = models.CharField(verbose_name='dekor', max_length=20, blank = True, choices=DEKOR)
    cake_inscription = models.CharField(verbose_name='inscription', max_length=100, blank = True)
    cake_comment = models.CharField(verbose_name='comment', max_length=255, blank = True)

    def __str__(self):
        return f'{self.cake_level} {self.cake_form} {self.cake_topping} {self.cake_berries} {self.cake_dekor} {self.cake_inscription} {self.cake_comment}'


# class Сake_buyer(models.Model):
#     cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
#     buyer_name = models.CharField('ФИО', max_length=200)
#     buyer_mail = models.EmailField(max_length=254)
#     buyer_phone = models.CharField('промокод', max_length=10)
#     buyer_date = models.DateField('дата заказа', null=True)
#     buyer_discount = models.CharField('промокод', max_length=10, blank = True)
