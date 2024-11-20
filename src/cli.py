import click


@click.group("cli")
@click.pass_context
def cli(ctx):
   click.echo("Inside cli")
   ctx.obj = "cli"
 

 
if __name__ == '__main__':
   cli()