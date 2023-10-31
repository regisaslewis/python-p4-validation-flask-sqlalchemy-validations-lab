from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if not bool(name):
            raise ValueError("Must have a name.")
        
    @validates("phone_number")
    def validate_phone_number(self, key, number):
        digits = number.replace("-", "")
        if len(digits) != 10:
            raise ValueError("Phone number must bet 10 digits.")

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("title")
    def validate_title(self, key, title):
        phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        count = 0
        for n in phrases:
            if n in title:
                count += 1
        if not bool(title):
            raise ValueError("Must have title.")
        elif count < 1:
            raise ValueError("Title isn't clickbait.")
    
        
    @validates("content")
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Content is too short.")
        
    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary is too long.")
    
    @validates("category") 
    def validate_category(self, key, category):
        categories = ["Fiction", "Non-Fiction"]
        if category not in categories:
            raise ValueError("Not an acceptable category.")
        

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
