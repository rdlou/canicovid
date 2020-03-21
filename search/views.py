from django.shortcuts import render, redirect
from search.documents import QuestionDocument
from questions.models import Question, Answer
from questions.question_formatter import formatter
# Create your views here.

def search(request):

    q = request.GET.get('q')

    response = {'user_q' : q,
                'questions':''}

    if q:

        questions = QuestionDocument.search().query("match", question= q)
        if not questions:
            q = formatter(q)
            questions = QuestionDocument.search().query("match", question={"query": q, "fuzziness":4})    
    else:
        questions = ''

    response['questions'] = questions

    print(response)

    return render(request, 'search/search.html', response)


def thumbs_up(request):
    answer_id = request.GET.get('answer_id')
    question = request.GET.get('q')

    qs = Question.objects.filter(question=question)
    if qs.count() == 0:
        new_question = Question()
        new_question.question = question

        answer = Answer.objects.get(pk=answer_id)

        new_question.answer = answer
        new_question.save()

    return redirect('/search')

