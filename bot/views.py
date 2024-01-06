from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

# Training the bot
list_to_train = [
    "hi",
    "hi, there",
    "what's your name?",
    "I'm just a chatbot",
    "what is your fav food ?",
    "I like cheese",
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request, 'bot/index.html')

def specific(request):
    number = 5
    return HttpResponse(number)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    # Get bot's response
    bot_response = bot.get_response(userMessage)
    return HttpResponse(bot_response)
