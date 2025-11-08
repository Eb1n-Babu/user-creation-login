from django.shortcuts import render
from polls.models import Question, Choice


# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})
def details(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        return render(request, 'details.html', {'question': question})
    except Question.DoesNotExist:
        return render(request, '404.html')

def choices(request, question_id):
    choice = Choice.objects.filter(question_id=question_id)
    return render(request, 'details.html.', {'choice': choice})