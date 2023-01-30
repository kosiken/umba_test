import argparse
import sys
import requests
from os import getcwd
from sqlalchemy import desc

sys.path.insert(0, getcwd())

try:
    from app.server import app, db
    from app.models import User
except ImportError:
    raise ImportError('Cannot find `app` module are you running from the root directory')


def get_users(amount: int, skip=0):
    limit = 100
    remaining = amount
    if amount < 100:
        limit = amount
    last = skip
    users = []
    while remaining > 0:
        response = requests.request(method='GET', url='https://api.github.com/users',
                                    params={'per_page': limit, 'since': last}).json()
        users = users + response
        users_length = len(users)
        remaining = amount - users_length
        if remaining < 100:
            limit = remaining
        last = users[users_length - 1]['id']

    return users


def init_db():
    with app.app_context():
        db.metadata.create_all(bind=db.engine, checkfirst=True)

        print('init complete {}'.format(db.engine.url))


def seed_database(number):
    init_db()
    last = 0
    with app.app_context():
        # first try to find if we have added users
        # before
        prev = db.session.execute(
            db.select(User).order_by(desc(User.id)).limit(1)
        )
        first = prev.scalar()
        if first is not None:
            # If we have then we need to add users after this user id
            last = first.id
            print('Db is not empty, query from {}'.format(last))
            pass

        users = get_users(number, last)
        users_to_add = [User(**row) for row in users]
        db.session.add_all(users_to_add)
        db.session.commit()



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Database Seeder')
    parser.add_argument('-t', '--total', dest='total', type=int, default='150', help="Number of users to seed")
    args = parser.parse_args()

    num_of_users = 150
    try:
        num_of_users = int(args.total)
        seed_database(num_of_users)
    except TypeError as e:
        print(e, 'll')
        print('Expected total to be a number, got \'{}\''.format(args.total))
    except ValueError as v:
        print(v)
        print('Expected total to be a number, got \'{}\''.format(args.total))
