from . import db
from werkzeug.security import generate_password_hash,check_password_hash


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
    pass_secure = db.Column(db.String(255))

    @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'username:{self.username}'
