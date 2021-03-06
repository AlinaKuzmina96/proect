from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage

# Create your views here. 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


#def paginate(request, qs):
    #try:
        #limit = int(request.GET.get('limit', 10))
    #except ValueError:
     #   limit = 10
    #if limit > 20:
     #   limit = 10
    #try:
     #   page = int(request.GET.get('page', 2))
    #except ValueError:
     #   raise Http404
    #except TypeError:
     #   raise Http404
    #paginator = Paginator(qs, limit)
    #try:
     #   page = paginator.page(page)
    #except EmptyPage:
     #   page = paginator.page(paginator.num_pages)
    #return paginator, page

def main_page(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    #except ValueError:
        #raise Http404
    questions = Question.objects.all().order_by('-id')
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    #paginator, page = paginate(request,questions)
    return render(request, 'list.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page,
        })

def popular(request):
    try:
        page = int(request.GET.get('page'))
    #except ValueError:
        #raise Http404
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    #paginator, page = paginate(request,questions)
    return render(request, 'list.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page,
        })
               
def question(request, num):
    question = get_object_or_404(Question, id=num)
    #try:
       # question = Question.objects.get(id=num)
    #except Question.DoesNotExist:
      #  raise Http404
    answers = Answer.objects.filter(question=question.pk).order_by('-added_at')[0:10]
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        })
