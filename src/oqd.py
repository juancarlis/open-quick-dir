import click
from pathlib import Path

from src.dirs import commands as dir_commands
from src.navigation import commands as nav_commands


DIRS_TABLE = Path("~/.local/share/oqd/directories.csv").expanduser()


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj["dirs_table"] = DIRS_TABLE

    # Creating database if not exists
    DIRS_TABLE.parent.mkdir(parents=True, exist_ok=True)

    if not DIRS_TABLE.exists():
        DIRS_TABLE.touch()


cli.add_command(dir_commands.all)
cli.add_command(nav_commands.all)
