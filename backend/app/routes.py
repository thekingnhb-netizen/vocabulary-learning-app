from flask import Flask
from app.utils.response import error_response


def register_routes(app: Flask):
    from app.controllers.topic_controller import topic_bp
    from app.controllers.vocabulary_controller import vocabulary_bp
    from app.controllers.review_controller import review_bp

    app.register_blueprint(topic_bp, url_prefix='/api')
    app.register_blueprint(vocabulary_bp, url_prefix='/api')
    app.register_blueprint(review_bp, url_prefix='/api')

    @app.errorhandler(404)
    def not_found(_):
        return error_response('Resource not found', 404)

    @app.errorhandler(400)
    def bad_request(_):
        return error_response('Bad request', 400)

    @app.errorhandler(500)
    def internal_error(_):
        return error_response('Internal server error', 500)
