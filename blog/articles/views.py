from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

from blog.models import Article, Author, Tag
from blog.forms.article import CreateArticleForm
from blog.extensions import db

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')





@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


# @article.route('/create', methods=['GET'])
# @login_required
# def create_article_form():
#     form = CreateArticleForm(request.form)
#     return render_template('articles/create.html',form=form)


@article.route('/create', methods=['POST','GET'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == "POST" and form.validate_on_submit():
        _article = Article(title=form.title.data.strip(),text=form.text.data)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_article',pk =_article.id))
    return render_template('articles/create.html',form=form)
    

@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        selected_artical: Article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
        if not selected_artical:
            raise NotFound(f"Article #{pk} doesn't exist!")

        author_row = Author.query.filter_by(id=selected_artical.author_id).one_or_none()
        if author_row != None:
            name_user =f'{ author_row.user.first_name} { author_row.user.last_name}'
        else:
            name_user = 'None'
    except KeyError:
         return redirect(
            '/articles/'
        )

    return  render_template(
        'articles/details.html',
        article_object = selected_artical,
        name_user = name_user
    )
