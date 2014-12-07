import json as simplejson
from django.shortcuts import render, redirect
from django.http import HttpResponse
from voogasalad.models import Game

def get_num_players(request):
	current_game = Game.objects.last()
	return HttpResponse(current_game.num_players)

def join_game(request):
	current_game = Game.objects.last()
	current_game.num_players += 1
	current_game.save()
	return HttpResponse(current_game.game_directory)

def make_game(request):
	if request.method == 'POST':
		game_dir = request.POST['game_directory']
		print 'h1'
		game = Game.objects.create(game_directory=game_dir)
		print 'hello'
		return HttpResponse("Success")

def get_master_json(request):
	current_game = Game.objects.last()
	return HttpResponse(current_game.master_json)

def get_and_clear_new_towers(request):
	current_game = Game.objects.last()
	secondary_json = current_game.secondary_json
	current_game.secondary_json = ""
	current_game.save()
	return HttpResponse(secondary_json)

def update_secondary_json(request):
	if request.method == 'POST':
		secondary_json = request.POST['new_towers']
		current_game = Game.objects.last()
		current_game.secondary_json = secondary_json
		current_game.save()
		return HttpResponse("Success")

def update_master_json(request):
	if request.method == 'POST':
		master_json = request.POST['master_json']
		current_game = Game.objects.last()
		current_game.master_json = master_json
		current_game.save()
		return HttpResponse("Success")