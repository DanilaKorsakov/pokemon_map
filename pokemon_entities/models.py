from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, default='', verbose_name='Название анг.')
    title_jp = models.CharField(max_length=200, default='', verbose_name='Название яп.')
    image = models.ImageField(upload_to='pokemons', blank=True, verbose_name='Изображение')
    description = models.TextField( default='', verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        "Pokemon",
        verbose_name='Предыдущая эволюция',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name="next_evolution",
    )

    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=datetime.now, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(default=datetime.now, verbose_name='Время исчезновения')
    level = models.IntegerField(default=1, verbose_name='Уровень')
    health = models.IntegerField(default=1, verbose_name='Здоровье')
    strength = models.IntegerField(default=1, verbose_name='Сила')
    defence = models.IntegerField(default=1, verbose_name='Защита')
    stamina = models.IntegerField(default=1, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon}: {self.lat}, {self.lon}"