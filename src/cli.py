import click

@click.group("cli")
@click.pass_context
def cli(ctx):
   click.echo("Inside cli")
   ctx.obj = "cli"
   ctx.obj = ["hello", "world"]
   _dict = {"Hello": "World", "statement": "lol"}
   ctx.obj = _dict

@cli.command("info")
def info():
    """Standalone command with no flags or arguments."""
    click.echo("Info command executed")

@cli.group()
def akte():
    """Command group for akte operations."""
    pass

@cli.group()
def register():
    """Command group for register operations."""
    pass

@cli.group()
def dokument():
    """Command group for dokument operations."""
    pass

def crud_commands(group):
    @group.command("create")
    @click.option('--obId', '--obid', required=True, help='Object ID')
    @click.option('--p', is_flag=True, help='Print to screen')
    @click.option('--log', help='Log file path')
    @click.pass_context
    def create(ctx, obid, p, log):
        click.echo(ctx.obj)
        click.echo(f"Creating {group.name}: obId={obid}, print={p}, log={log}")

    @click.pass_context
    def read(ctx, filepath , p, log):
        click.echo(ctx)
        click.echo(f"Reading {group.name}:filepath={filepath}, print={p}, log={log}")

    @click.pass_context
    def update(ctx,filepath, p, log):
        click.echo(ctx)
        click.echo(f"Updating {group.name}: filepath={filepath}, print={p}, log={log}")

    @click.pass_context
    def delete(ctx, filepath, p, log):
        click.echo(ctx)
        click.echo(f"Deleting {group.name}: filepath={filepath}, print={p}, log={log}")

    for cmd in [read, update, delete]:
        group.command()(click.option('--filepath', required=False, help='File path')(
            click.option('--p', is_flag=True, help='Print to screen')(
                click.option('--log', help='Log file path')
                (cmd))))

# Apply CRUD commands to each group
for group in [akte, register, dokument]:
    crud_commands(group)

@cli.command("check_context_object")
@click.pass_context
def check_context(ctx):
   print(type(ctx.obj))
   print(ctx.obj)

pass_dict = click.make_pass_decorator(dict)

@cli.command("get_keys")
@pass_dict
def get_keys(_dict):
   keys = list(_dict.keys())
   click.secho("The keys in our dictionary are", fg="green")
   click.echo(click.style(keys, fg="blue"))

if __name__ == '__main__':
   cli()