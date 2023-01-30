from flask import make_response, request
from app.server import db, cache
from app.models import User


class UserApiController:

    @staticmethod
    @cache.cached(timeout=30, query_string=True)
    def api_fetch_users():
        current_page = 1
        limit = 25
        order_by = 'id'
        query = db.select(User)
        query_dict = {key: value for key, value in request.args.items()}

        try:
            page = (query_dict.get('page'))
            pagination = query_dict.get('pagination')
            order_by = query_dict.get(order_by)
            user_id = query_dict.get('id')
            username = query_dict.get('username')

            if user_id is not None:
                id_filter = int(user_id)
                query = query.where(User.id == id_filter)

            if username is not None:
                query = query.where(User.login == username)

            if order_by is None:
                order_by = 'id'
            if page is not None:
                current_page = int(page)
            if pagination is not None:
                limit = int(pagination)
        except Exception as e:
            print(e)
            pass
        paginate = db.paginate(query.order_by(order_by), per_page=limit, page=current_page)

        payload = {'type': 'success', 'message': 'fetch_users', 'data': {
                'rows': [i.as_dict() for i in paginate.items],
                'page': paginate.page,
                'pages': paginate.pages,
                'per_page': limit,
                'total': paginate.total
        }}
        return make_response(payload, 200)
