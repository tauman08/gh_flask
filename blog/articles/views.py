from flask import Blueprint, render_template, redirect
from flask_login import login_required

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

from blog.models import User

ARTICLES = {
    1: {'name':'Премия дарвина','user_id':1,'text':"""Турист из Тулы насмерть замерз на Эльбрусе. Об этом сообщает Telegram-канал 112.
    Отмечается, что 37-летний Сергей Гавриков решил подняться на вершину в кроссовках. На кадрах видно, что мужчина не взял с собой
    никакого снаряжения — у него был только рюкзак.
    По словам супруги, 27 февраля мужчина должен был вернуться домой, однако по непонятным причинам сдал билеты.
    После Гавриков перестал выходить на связь. 3 марта тело пропавшего россиянина обнаружили спасатели на высоте 5 тысяч метров.
    25 февраля альпинист из Читы скончался во время восхождения на Эльбрус. Предположительная причина смерти — сердечный приступ.
    Отмечается, что группа состояла из пяти человек."""},
    2: {'name':'Литералы строк','user_id':2,'text':""" Работа со строками в Python очень удобна. Существует несколько 
        литералов строк, которые мы сейчас и рассмотрим.
            Строки в апострофах и в кавычках
            S = 'spam"s'
            S = "spam's"
        Строки в апострофах и в кавычках - одно и то же. Причина наличия двух вариантов в том, 
        чтобы позволить вставлять в литералы строк символы кавычек или апострофов, не используя экранирование."""},
    3: {'name':'State_3','user_id':3,'text':'skjldfhds hsjddfdksljfh sdkjfhsdkljfkl jslkdjfh lkjhlksjdhf slkdjfh'},
}

@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )

@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article_object = ARTICLES[pk]
        user_row = User.query.filter_by(id=article_object['user_id']).one_or_none()
        if user_row != None:
            name_user = user_row.email
        else:
            name_user = 'None'
    except KeyError:
        # raise NotFound(f'Article id {pk} not found')
        return redirect(
            '/articles/'
        )

    return  render_template(
        'articles/details.html',
        article_object = article_object,
        name_user = name_user
    )
