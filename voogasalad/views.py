import json as simplejson
from django.shortcuts import render, redirect
from django.http import HttpResponse
from voogasalad.models import Game

def make_game(request):
	if request.method == 'POST':
		game_dir = request.POST['game_directory']
		game = Game.objects.create(game_directory=game_dir)

def get_master_json(request):
	current_game = Game.objects.last()
	return HttpResponse(current_game.master_json, 
						content_type="application/json")

def update_master_json(request):
	if request.method == 'POST':
		master_json = request.POST['master_json']
		current_game = Game.objects.last()
		current_game.master_json = master_json
		current_game.save()