from logging import basicConfig, ERROR

from app.utils import cli
basicConfig(level=ERROR)
if __name__ == "__main__":
    cli.cli()
