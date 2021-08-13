from flask import Flask

# Initializing app
app = Flask(__name__)
 
 def create_app():


# Registering the blueprint
from .main import main as main blueprint
app.register_blueprint(main_blueptint)


return app