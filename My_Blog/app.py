from flask import Flask, render_template,redirect, url_for, request, flash
import datetime as dt
import smtplib
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from flask import abort
from flask_ckeditor import CKEditor
from forms import CommentForm


connection = smtplib.SMTP("smtp.gmail.com", port=587)

OWN_EMAIL = "ellizabetta.fadeeva@gmail.com"
OWN_PASSWORD = "sasjkhjasj"

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key-goes-here'
db = SQLAlchemy(app)
Bootstrap(app)
ckeditor = CKEditor(app)

login_manager = LoginManager()
login_manager.init_app(app)

POSTS_PER_PAGE = 3


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
    
    def __repr__(self):
        return '<Username %r>' %self.username
    

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False, default = dt.datetime.utcnow)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="parent_post")
    
    
    def __repr__(self):
        return '<Blog %r>' % self.id

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
   
    

# with app.app_context():     
#     db.create_all()

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=POSTS_PER_PAGE)
    return render_template("index.html", posts=posts, logged_in=current_user.is_authenticated)

@app.route('/about')
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)

@app.route('/contact')
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)

@app.route('/create', methods = ['GET', 'POST'])
@admin_only
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        img_url = request.form['img-url']
        body = request.form['body']
        post=BlogPost(title=title,subtitle=subtitle,body=body,img_url=img_url)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return " There is an error during posting a Post"
    else:
        return render_template("create_post.html", logged_in=current_user.is_authenticated)

@app.route("/post/<int:id>",methods=["GET", "POST"])
def show_post(id):
    comment_form = CommentForm()
    post = BlogPost.query.get(id)
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=post, form=comment_form, current_user=current_user)

@app.route("/posts/<int:id>/delete")
@admin_only
def post_delete(id):
    post = BlogPost.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')
    except:
        return "There is an error during deleting a Post"


   
@app.route("/posts/<int:id>/edit", methods = ['GET', 'POST'])
@admin_only 
def post_edit(id):
    post = BlogPost.query.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.subtitle = request.form['subtitle']
        post.img_url = request.form['img-url']
        post.body = request.form['body']
        post.date = request.form['date']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return " There is an error during editing a Post"
    else:
        
        return render_template("post_update.html", post=post, logged_in=current_user.is_authenticated)
    
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            username=request.form.get('username'),
            password=hash_and_salted_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        
        return redirect("/")

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        #Find user by email entered.
        user = User.query.filter_by(email=email).first()
        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect("/")
          
    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
        

@app.route('/message', methods = ['POST'])
def send_message():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
    



if __name__=="__main__":
    app.run
    