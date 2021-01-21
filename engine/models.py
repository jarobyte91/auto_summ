from engine import db

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Query {}>'.format(self.id)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    summary = db.Column(db.String)
    relevance = db.Column(db.Integer)

    def __repr__(self):
        return '<Response {}>'.format(self.id)
