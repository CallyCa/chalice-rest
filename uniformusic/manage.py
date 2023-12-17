import click
from flask.cli import FlaskGroup

from uniformusic.app import create_app
from uniformusic.config import ADMIN_PASSWORD


def create_uniformusic():
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_uniformusic)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    """
    from uniformusic.extensions import db
    from uniformusic.models import User
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password=ADMIN_PASSWORD,
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
