from app import create_app, db
from app.routes import *

app = create_app()
app.register_blueprint(bp, url_prefix="/api")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
