from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, default='')
    title_jp = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='pokemons', blank=True)
    description = models.TextField(default='')
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
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=datetime.now)
    disappeared_at = models.DateTimeField(default=datetime.now)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pokemon}: {self.lat}, {self.lon}"