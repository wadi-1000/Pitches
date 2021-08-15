from . import db

class Pitch:

    all_pitches = []

    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
       

    def save_pitch(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'username:'{self.username}