import click

from src.dirs import commands as dir_commands
from src.navigation import commands as nav_commands


DIRS_TABLE = ".directories.csv"


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj["dirs_table"] = DIRS_TABLE


cli.add_command(dir_commands.all)
cli.add_command(nav_commands.all)
