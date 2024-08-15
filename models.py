from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    progress = db.relationship('Progress', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(140))
    score = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Progress {self.topic} - {self.score}>'
