from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(request):

    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    '''A Segunda pagina do site'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def new_topic(request):
    '''Terceira pagina do site'''
    return render(request, 'learning_logs/exemplo 11.html')


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
