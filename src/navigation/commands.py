import click
import os
import subprocess

from src.dirs.services import DirService


@click.command()
@click.argument("dir_name_or_quick_access")
@click.option("-h", "horizontal", is_flag=True, help="Open in horizontal split in tmux")
@click.option("-v", "vertical", is_flag=True, help="Open in vertical split in tmux")
@click.option("-w", "new_window", is_flag=True, help="Open in a new window in tmux")
@click.pass_context
def nav(ctx, dir_name_or_quick_access, horizontal, vertical, new_window):
    """Navigate to a directory."""
    dir_service = DirService(ctx.obj["dirs_table"])
    path = dir_service.get_directory_path(dir_name_or_quick_access)

    if not path:
        click.echo(f"Directory {dir_name_or_quick_access} not found.")
        return

    if horizontal:
        subprocess.run(["tmux", "split-window", "-h"])
        subprocess.run(["tmux", "send-keys", f"cd {path}", "Enter"])
    elif vertical:
        subprocess.run(["tmux", "split-window", "-v"])
        subprocess.run(["tmux", "send-keys", f"cd {path}", "Enter"])
    elif new_window:
        subprocess.run(["tmux", "new-window"])
        subprocess.run(["tmux", "send-keys", f"cd {path}", "Enter"])

    else:
        subprocess.run(["tmux", "send-keys", f"cd {path}", "Enter"])


all = nav
