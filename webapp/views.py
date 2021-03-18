from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    try:
        prev = 0
        next = 0
        prev_page = True
        next_page = True
        if question_id > 1 and question_id < len(Question.objects.all()):
            prev = question_id-1
            next = question_id+1
        elif question_id > 1 and question_id == len(Question.objects.all()):
            prev = question_id-1
            next_page = False
        else:
            if len(Question.objects.all())==1:
                prev_page = False
                next_page = False
            else:
                next = question_id+1
                prev_page = False
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'webapp/detail.html', {'question': question,
     'prev': prev, 'next': next, 'prev_page': prev_page,
     'next_page': next_page})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question_id == len(Question.objects.all()):
        pass
    else:
        next = question_id+1
        next_page = True
    return render(request, 'webapp/results.html', {'question': question, 'next': next,
    'next_page': next_page})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'webapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('webapp:results', args=(question.id,)))

def overview(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    questions = Question.objects.all()
    content = {}
    for q in questions:
        content[q] = q.max_vote()
        list(content)
        return render(request, 'webapp/overview.html', {'content':content[q],
        'latest_question_list': latest_question_list})

    
    # return render(request, 'webapp/overview.html', {'content':content,
    # 'latest_question_list': latest_question_list})

