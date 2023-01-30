from flask import render_template, request

from app.utils import PageItem
from app.server import db
from app.models import User


class UserController:

    @staticmethod
    def index_page():

        paginate = db.paginate(db.select(User), per_page=25, page=1)
        paginate_items = PageItem.create_page_items(paginate.page, paginate.pages)

        return render_template('pages/index.html', users=paginate.items, page=paginate.page, per_page=35,
                               pages=paginate.pages,
                               has_next=paginate.has_next, has_prev=paginate.has_prev, paginate_items=paginate_items)

    @staticmethod
    def fetch_users(page='1'):
        current_page = 1
        limit = 25
        query_dict = {key: value for key, value in request.args.items()}
        try:
            current_page = int(page)
            pagination = query_dict.get('pagination')
            if pagination is not None:
                limit = int(pagination)
        except Exception:
            pass
        if limit > 100:
            limit = 100
        paginate = db.paginate(db.select(User), per_page=limit, page=current_page)
        paginate_items = PageItem.create_page_items(paginate.page, paginate.pages)


        return render_template('pages/users.html', users=paginate.items, page=paginate.page, per_page=limit,
                               pages=paginate.pages,
                               has_next=paginate.has_next, has_prev=paginate.has_prev, paginate_items=paginate_items)
