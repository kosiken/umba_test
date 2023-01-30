from app.server import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    node_id = db.Column(db.String)
    login = db.Column(db.String, unique=True, index=True, nullable=False)
    avatar_url = db.Column(db.String)
    gravatar_id = db.Column(db.String)
    url = db.Column(db.String)
    html_url = db.Column(db.String)
    followers_url = db.Column(db.String)
    gists_url = db.Column(db.String)
    starred_url = db.Column(db.String)
    subscriptions_url = db.Column(db.String)
    repos_url = db.Column(db.String)
    events_url = db.Column(db.String)
    received_events_url = db.Column(db.String)
    type = db.Column(db.String)
    site_admin = db.Column(db.Boolean, default=False)
    following_url = db.Column(db.String)
    organizations_url = db.Column(db.String)




