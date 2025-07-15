from flask import Flask
from flasgger import Swagger
from routes.datasets import datasets_blueprint
from routes.quality_logs import quality_logs_blueprint

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Configure Swagger for API documentation
    Swagger(app)

    # Register blueprints for routes
    app.register_blueprint(datasets_blueprint)
    app.register_blueprint(quality_logs_blueprint)

    return app

if __name__ == '__main__':
    # Create and run the Flask app
    app = create_app()
    app.run(debug=True)
