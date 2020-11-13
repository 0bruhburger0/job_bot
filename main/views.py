from django.shortcuts import render, redirect
from .models import Questions, Vacancy, Resume
from .management.commands import bot


def home(request):
    data = {'title': 'Главная'}
    return render(request, 'main/main.html', data)


def vacancy(request):
    data = {'title': 'Вакансии',
            'vacancy': Vacancy.objects.all()}
    return render(request, 'main/vacancy.html', data)


def del_vacancy(request):
    values = request.POST.getlist('some_name')
    Vacancy.objects.filter(tg_id__in=values).delete()
    return redirect('http://127.0.0.1:8000/main/vacancy/')


def send_vacancy(request):
    tg_id = int(request.POST.get('somes'))
    m = Vacancy.objects.filter(tg_id=tg_id)
    m.update(status=True)
    # all_part = Vacancy.objects.filter(tg_id=tg_id).all()
    bot.send_vacancy(tg_id)

    return redirect('http://127.0.0.1:8000/main/vacancy/')


def resume(request):
    data = {'title': 'Резюме',
            'resume': Resume.objects.all()}
    return render(request, 'main/resume.html', data)


def del_resume(request):
    values = request.POST.getlist('some_name')
    Resume.objects.filter(tg_id__in=values).delete()
    return redirect('http://127.0.0.1:8000/main/resume/')


def send_resume(request):
    tg_id = int(request.POST.get('somes'))
    m = Resume.objects.filter(tg_id=tg_id)
    m.update(status=True)
    # all_part = Vacancy.objects.filter(tg_id=tg_id).all()
    bot.send_resume(tg_id)

    return redirect('http://127.0.0.1:8000/main/resume/')


def questions(request):
    data = {'title': 'Вопросы',
            'questions': Questions.objects.all()}
    return render(request, 'main/questions.html', data)


def del_questions(request):
    values = request.POST.getlist('some_name')
    Questions.objects.filter(tg_id__in=values).delete()
    return redirect('http://127.0.0.1:8000/main/questions/')


# def send_questions(request):
#     tg_id = int(request.POST.get('tg_id'))
#     id_bd = int(request.POST.get('id_bd'))
#     print(id_bd)
#     text = request.POST.get('answer')
#     question = request.POST.get('question')
#     m = Questions.objects.filter(id=id_bd)
#     m.update(answer=text)
#     bot.send_questions(tg_id, question, text)
#
#     return redirect('http://127.0.0.1:8000/main/resume/')


def make_answer(request):
    id_bd = request.POST.get("id_bd")
    tg_id = request.POST.get("tg_id")
    question = request.POST.get("question")
    data = {
        'id_bd': id_bd,
        'tg_id': tg_id,
        'question': question,
        'title': 'Ответ'}
    return render(request, 'main/make_answer.html', data)


def send_answer(request):
    tg_id = int(request.POST.get('tg_id'))
    id_bd = int(request.POST.get('id_bd'))
    print(id_bd)
    text = request.POST.get('answer')
    question = request.POST.get('question')
    m = Questions.objects.filter(id=id_bd)
    m.update(answer=text)
    bot.send_questions(tg_id, text, question)
    return redirect('http://127.0.0.1:8000/main/questions/')


def del_question(request):
    values = request.POST.getlist('some')
    Questions.objects.filter(id__in=values).delete()
    return redirect('http://127.0.0.1:8000/main/questions/')