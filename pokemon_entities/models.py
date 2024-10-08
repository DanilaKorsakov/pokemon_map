from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, verbose_name='Название анг.', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Название яп.', blank=True)
    image = models.ImageField(upload_to='pokemons', blank=True, verbose_name='Изображение')
    description = models.TextField( verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon",
        verbose_name='Предыдущая эволюция',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name="next_evolutions",
    )

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities'
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень', blank=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True)
    strength = models.IntegerField( verbose_name='Сила', blank=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True)

    def __str__(self):
        return f"{self.pokemon}: {self.lat}, {self.lon}"