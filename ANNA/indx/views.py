from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return render(request, 'indx/index.html')

def photosView(request):
    return render(request, 'indx/photos.html')

def testView(request):
    return render(request, 'indx/test.html')

def questionsView(request):
    return render(request, 'indx/main_test.html')

def resultView(request):

    if request.method == 'POST':

        user_answers = {}
        correct_answers = {
            'q1': 'q14',
            'q2': 'q23',
            'q3': 'q32',
            'q4': 'q44',
            'q5': 'q53',
            'q6': 'q63',
            'q7': 'q72',
            'q8': 'q84',
            'q9': 'q92',
            'q10': 'q105',
            'q11': 'q111',
        }

        context = {
            'procent': 0,
            'correct_questions': '',
            'uncorrect_questions': '',
        }

        user_score = 0

        for i in range(11):
            user_answers['q'+str(i+1)] = request.POST.get('q'+str(i+1))
        
        for i in correct_answers:
            if correct_answers[i] == user_answers[i]:
                user_score += 1
                context['correct_questions'] += f"{str(i.split('q')[1])} "
            else:
                context['uncorrect_questions'] += f"{str(i.split('q')[1])} "

        context['procent'] = round((user_score*100)/11, 1)
        

    return render(request, 'indx/results.html', context)