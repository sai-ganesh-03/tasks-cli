import click

from utils.utils import add_todo,list_todos,delete_todo,update_todo_description,update_todo_status_done,update_todo_status_progress

@click.group()
def cli():
    pass

@cli.command()
@click.argument('todo_description')
def add(todo_description):
    todo_id=add_todo(todo_description)
    click.echo(f'Task added successfully (ID: {todo_id})')

@cli.command()
@click.argument("status",required=False)
def list(status):
   todo_list_str=list_todos(status)
   click.echo(todo_list_str)
   
@cli.command()
@click.argument("id")
def delete(id):
    try:
       todo_id=delete_todo(int(id))
       click.echo(f'Task deleted successfully (ID: {todo_id})')
    except ValueError:
       click.echo("Invalid ID. Please provide a valid integer.")
       
@cli.command()
@click.argument("todo_id")
@click.argument("todo_description")
def update(todo_id,todo_description):
    try:
        todo_id=update_todo_description(int(todo_id),todo_description)
    except ValueError:
        click.echo("Invalid ID. Please provide a valid integer.")
        
    if todo_id:
        click.echo(f'Task updated successfully (ID: {todo_id})')
    else:
        click.echo("Task not found.")
    
    
@cli.command(name="mark-in-progress")
@click.argument("todo_id")
def mark_in_progress(todo_id):
    try:
        todo_id=update_todo_status_progress(int(todo_id))
    except ValueError:
        click.echo("Invalid ID. Please provide a valid integer.")
        
    if todo_id:
        click.echo(f'Task status updated to in-progress (ID: {todo_id})')
    else:
        click.echo("Task not found.")

@cli.command(name="mark-done")
@click.argument("todo_id")
def mark_done(todo_id):
    try:
        todo_id=update_todo_status_done(int(todo_id))
    except ValueError:
       click.echo("Invalid ID. Please provide a valid integer.")
       
    if todo_id:
        click.echo(f'Task status updated to done (ID: {todo_id})')
    else:
        click.echo("Task not found.")
   
if __name__ == '__main__':
    cli()
