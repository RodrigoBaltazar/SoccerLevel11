from flask import Blueprint

from .views import index, video

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/video/<video_id>", view_func=video, endpoint="videoview"
)


def init_app(app):
    app.register_blueprint(bp)