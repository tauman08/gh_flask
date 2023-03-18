from flask import Blueprint, render_template, request, redirect, url_for
from blog.models import Article,  Tag

tag = Blueprint('tag', __name__, url_prefix='/tags', static_folder='../static')


@tag.route('/')
def tag_list():
    tags: Tag = Tag.query.all()
    return render_template(
        'tags/list.html',
        tags=tags,
    )


@tag.route('/<int:pk>')
def tag_details(pk: int):
    selected_tag = Tag.query.filter_by(id=pk).one_or_none()
    if not selected_tag:
        raise NotFound(f"Tag #{pk} doesn't exist!")

    return render_template(
        'tags/details.html',
        tag=selected_tag,
    )