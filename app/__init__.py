from flask import Flask as F
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = F(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
