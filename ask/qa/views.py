from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request):
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
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'list.html', {
        'paginator': paginator,
        'title': 'Latest',
        'questions': page.object_list,
        'page': page
        })


               
