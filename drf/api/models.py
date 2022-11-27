from django.db import models


class Cake(models.Model):
    NUMBER_LEVELS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]
    FORM = [
        ('Круг', 'Круг'),
        ('Квадрат', 'Квадрат'),
        ('Прямоугольник', 'Прямоугольник')
    ]
    TOPPING = [
        ('Без', 'Без'),
        ('Белый соус', 'Белый соус'),
        ('Карамельный', 'Карамельный'),
        ('Кленовый', 'Кленовый'),
        ('Черничный', 'Черничный'),
        ('Молочный шоколад', 'Молочный шоколад'),
        ('Клубничный', 'Клубничный'),
    ]
    BERRIES = [
        ('Ежевика', 'Ежевика'),
        ('Малина', 'Малина'),
        ('Голубика', 'Голубика'),
        ('Клубника', 'Клубника'),
    ]
    DEKOR = [
        ('Фисташки', 'Фисташки'),
        ('Безе', 'Безе'),
        ('Фундук', 'Фундук'),
        ('Пекан', 'Пекан'),
        ('Маршмеллоу', 'Маршмеллоу'),
        ('Марципан', 'Марципан')
    ]

    cake_level = models.CharField(
            verbose_name='level', max_length=1, choices=NUMBER_LEVELS,
            default='1'
    )

    cake_form = models.CharField(
            verbose_name='form', max_length=20, choices=FORM,
            default='Круг'
    )

    cake_topping = models.CharField(
            verbose_name='topping', max_length=50, choices=TOPPING,
            default='Ежевика'
    )

    cake_berries = models.CharField(
            verbose_name='berries', max_length=20, blank = True, choices=BERRIES
    )

    cake_dekor = models.CharField(
            verbose_name='dekor', max_length=20, blank = True, choices=DEKOR
    )

    cake_inscription = models.CharField(
            verbose_name='inscription', max_length=100, blank = True
    )

    def __str__(self):
        return f'Cake {self.pk}'


class User(models.Model):
    name = models.CharField(
        verbose_name='name', blank=True, null=True, max_length=50
    )
    phone = models.CharField(
        'phone', blank=True, null=True, max_length=50
    )
    email = models.EmailField(
        verbose_name='mail', blank=True, max_length=100,
        null=True, db_index=True,
    )
    address = models.TextField(
        verbose_name='address', blank=True, null=True,
    )
    orders = models.CharField(
        verbose_name='order', blank=True, max_length=50
    )

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    cake = models.ForeignKey(
            Cake, on_delete=models.CASCADE, null=True
            )
    date = models.DateField(verbose_name='Date delivery')
    time = models.TimeField(verbose_name='Time delivery')
    delivcomments = models.TextField(
        verbose_name='comment', blank=True
    )
    cost = models.IntegerField(
        verbose_name='price', null=True, blank=True,
    )

    def __str__(self):
        return f'Order {self.id}'