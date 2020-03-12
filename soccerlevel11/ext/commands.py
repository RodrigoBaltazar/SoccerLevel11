import click
from soccerlevel11.ext.database import db
from soccerlevel11.ext.auth import create_user
from soccerlevel11.models import Video


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Video(
            id=1, name="007", description="Contra Golden Eye"
        )
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Video.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)