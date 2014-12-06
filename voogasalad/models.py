from django.db import models

class Game(models.Model):
	game_directory = models.CharField(max_length=256)
  	master_json = models.TextField(null=True, blank=True)
  	secondary_json = models.TextField(null=True, blank=True)
