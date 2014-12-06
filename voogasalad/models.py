from django.db import models
from jsonfield import JSONField

class Game(models.Model):
  	master_json = JSONField()
  	secondary_json = JSONField()
