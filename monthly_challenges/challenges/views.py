from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenge = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Read a book each week!",
    "may": "Take cold showers!",
    "june": "Write a journal every day!",
    "july": "Meditate for 10 minutes a day!",
    "august": "Practice coding daily!",
    "september": "Go to bed before 11 PM!",
    "october": "Limit screen time to 2 hours a day!",
    "november": "Say something nice to someone each day!",
    "december": None  # Could mean no challenge or a surprise
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if (month > len(months)):
        return HttpResponseNotFound('Invalid Month')
    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)

def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenge[month]
        return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound('This month is not supported')