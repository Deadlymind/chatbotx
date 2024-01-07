from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .intents import intents

# Create your views here.

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])


list_trainer = ListTrainer(bot)

def train_chatbot(intents):
    for intent in intents:
        patterns = intent['patterns']
        responses = intent['responses']
        for pattern in patterns:
            list_trainer.train([pattern] + responses)

train_chatbot(intents)

def index(request):
    return render(request, 'bot/index.html')

def specific(request):
    number = 5
    return HttpResponse(number)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    response = bot.get_response(userMessage)
    return HttpResponse(response)
