from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', blank=True)
    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=datetime.now)
    disappeared_at = models.DateTimeField(default=datetime.now)

