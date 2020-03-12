from flask import abort, render_template
from soccerlevel11.models import Video


def index():
    videos = Video.query.all()
    return render_template("index.html", videos=videos)


def video(video_id):
    video = Video.query.filter_by(id=video_id).first() or abort(
        404, "video nao encontrado"
    )
    return render_template("video.html", video=video)


    