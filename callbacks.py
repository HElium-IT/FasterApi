import typer
from utils import delete_generated_files, revert_modified_files

def on_exception(exc: Exception):
    """
    Callback that is called when an exception is raised
    """
    typer.echo("An error has occurred")

    typer.echo("Deleting generated files...")
    delete_generated_files()

    typer.echo("Reverting modified files...")
    revert_modified_files()

    typer.echo("The error was:")
    typer.echo(exc)

    typer.echo("Exiting...")