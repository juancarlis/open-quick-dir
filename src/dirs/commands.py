import click


from src.dirs.services import DirService
from src.dirs.models import Directory


@click.group()
def dir():
    """dirs directories. CRUD."""
    pass


@dir.command()
@click.option("-n", "--name", type=str, prompt=True, help="The directory name")
@click.option("-p", "--path", type=str, prompt=True, help="The directory path")
@click.option(
    "-qa", "--quick-access", type=int, prompt=True, help="A number for quick access"
)
@click.pass_context
def new(ctx, name, path, quick_access):
    """Adds a new directory"""
    directory = Directory(name, path, quick_access)
    dir_service = DirService(ctx.obj["dirs_table"])

    dir_service.add_dir(directory)


@dir.command()
@click.pass_context
def list(ctx):
    """List all saved directories"""
    dir_service = DirService(ctx.obj["dirs_table"])

    dirs_list = dir_service.list_dirs()

    click.echo(" NAME | PATH | QUICK ACCESS ")
    click.echo("*" * 50)

    for dir in dirs_list:
        click.echo(
            "{name} | {path} | {quick_access}".format(
                name=dir["name"],
                path=dir["path"],
                quick_access=dir["quick_access"],
            )
        )


@dir.command()
@click.argument("dir_name", type=str)
@click.pass_context
def update(ctx, dir_name):
    """Updates a directory"""
    dir_service = DirService(ctx.obj["dirs_table"])
    dirs_list = dir_service.list_dirs()

    directory = [dir for dir in dirs_list if dir["name"] == dir_name]

    if directory:
        directory = _update_directory_flow(Directory(**directory[0]))
        dir_service.update_dir(directory, dir_name)

        click.echo("Directory updated")
    else:
        click.echo("Directory not found")


def _update_directory_flow(directory):
    click.echo("Leave empty if you dont want to modify the value")

    directory.name = click.prompt("New name", type=str, default=directory.name)
    directory.path = click.prompt("New path", type=str, default=directory.path)
    directory.quick_access = click.prompt(
        "New quick access", type=int, default=directory.quick_access
    )

    return directory


@dir.command()
@click.argument("dir_name", type=str)
@click.pass_context
def delete(ctx, dir_name):
    """Deletes a directory"""
    dir_service = DirService(ctx.obj["dirs_table"])
    dirs_list = dir_service.list_dirs()

    directory = [dir for dir in dirs_list if dir["name"] == dir_name]

    if directory:
        directory = Directory(**directory[0])
        dir_service.delete(directory)

        click.echo("Directory deleted")
    else:
        click.echo("Directory not found")


all = dir
