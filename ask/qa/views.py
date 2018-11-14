from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        raise Http404
    questions = Question.objects.new()
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'list.html', {
        'paginator': paginator,
        'title': 'Latest',
        'questions': page.object_list,
        'page': page,
        })

def popular(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        raise Http404
    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'list.html', {
        'paginator': paginator,
        'title': 'Popular',
        'questions': page.object_list,
        'page': page,
        })
               
def question(request, num):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.filter(question=question.pk).order_by('-added_at')[0:10]
    return render(request, 'question.html', {
        'question': q,
        'title': 'Question',
        'answers': answers,
        })
