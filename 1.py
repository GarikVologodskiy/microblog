from app import db
from app.models import User, Post

users = User.query.all()
print(users)


'''

#add users
from app import db
from app.models import User, Post

u = User(username='Rost', email='rost@gmail.com')
db.session.add(u)
db.session.commit()

---
from microblog import app
print(app.config['SECRET_KEY'])

---
from app.models import User, Post

u1 = User(username = 'Katrin', email = 'qwqwq@mail.com')

u2 = Post(body = 'Katrinblablabla')
print(u1)
print(u2)

users = User.query.all()
print(users)

for u in users:
    print(u.id, u.username, u.email)

u1 = User.query.get(1)
print(u1)

u = User.query.get(1)
p = Post(body='My delicious!', author=u)
db.session.add(p)
db.session.commit()


posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.author.email, p.body, sep = ', ')
    
>>> # get all posts written by a user
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
[<Post my first post!>]

>>> # same, but with a user that has no posts
>>> u = User.query.get(2)
>>> u
<User susan>
>>> u.posts.all()
[]

>>> # print post author and body for all posts 
>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
...
1 john my first post!

# get all users in reverse alphabetical order
>>> User.query.order_by(User.username.desc()).all()
[<User susan>, <User john>]

users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()
    
'''