from app.controllers.topic_controller import topic_bp
from app.controllers.vocabulary_controller import vocabulary_bp
from app.controllers.review_controller import review_bp
from app.utils.response import error_response
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(topic_bp, url_prefix="/api")
    app.register_blueprint(vocabulary_bp, url_prefix="/api")
    app.register_blueprint(review_bp, url_prefix="/api")

    @app.errorhandler(404)
    def handle_not_found(error):
        return error_response("Resource not found", 404)

    @app.errorhandler(400)
    def handle_bad_request(error):
        return error_response("Bad request", 400)

    @app.errorhandler(500)
    def handle_internal_error(error):
        return error_response("Internal server error", 500)
