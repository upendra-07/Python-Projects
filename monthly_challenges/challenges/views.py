from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    challenges_text = None
    if (month == 'january'):
        challenges_text = 'Welcome to January!!'
    elif (month == 'february'):
        challenges_text = 'Walk for atleast 20min every day'
    elif (month == 'march'):
        challenges_text = 'Learn Django for atleast 20 minutes every day!!'
    else:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(challenges_text)