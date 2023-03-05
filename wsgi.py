from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()

@app.cli.command('init-db')
def init_db():
    db.create_all()

@app.cli.command('create-user')
def create_users():
    from blog.models import User
    db.session.add(
        User(email='name@mail.com', password=generate_password_hash('test123'))
    )
    db.session.commit()

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug=True,)