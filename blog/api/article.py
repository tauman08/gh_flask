from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleListEvent(EventsResource):

    def event_get_count(self):
        return {'count': Article.query.count()}

    def event_get_api_server(self):
        return {'server': request.get('https://ifconfig.io/ip').text}

    def event_post_count(self):
        # просто для примера  как создать post. данный метод не работает
        return {'method': request.method}


class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self,  *args, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
