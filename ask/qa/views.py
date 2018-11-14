from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 2))
    except ValueError:
        raise Http404
    questions = Question.objects.all().order_by('-id')
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
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 3))
    except ValueError:
        raise Http404
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'list.html', {
        'paginator': paginator,
        'title': 'Popular',
        'questions': page.object_list,
        'page': page,
        })
               
def question(request):
    try:
        q = Question.objects.get(id=5)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {
        'question': q,
        'title': 'Question',
        })
