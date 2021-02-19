#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enquiries import choose
from enquiries import freetext
from enquiries import yesno
import sys
import click

@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', '--prompt', default='enter text: ')
@click.option('-q', '--quiet', is_flag=True)
def free(prompt, quiet):
    user_input = freetext(prompt)
    # If we're not being quiet and stdout is not being redirected, write the prompt
    if not quiet and sys.stdout.isatty():
        click.secho(prompt, err=True, bold=True)
    # always print the output
    click.echo(user_input)


@cli.command()
@click.option('-m', '--multiple-choice', is_flag=True, help='User can choose multiple options')
@click.option('-p', '--prompt', help='The message to display to the user')
@click.option('-q', '--quiet', is_flag=True, help='Clear the prompt after accepting choice')
@click.argument('options', nargs=-1)
def select(multiple_choice, quiet, prompt, options):
    choice = choose(prompt, options, multi=multiple_choice)
    # if not quiet, print everything
    if not quiet and prompt:
        click.secho(prompt + ' ', err=True, nl=multiple_choice, bold=True)
    # if we're being piped to somewhere else, always print choice
    if not quiet or not sys.stdout.isatty():
        if multiple_choice:
            # on multiple lines for multiple choices
            click.echo('\n'.join(choice))
        else:
            click.echo(choice)


@cli.command()
@click.option('-q', '--quiet', is_flag=True, help='Hide the prompt and response after accepting')
@click.option('-y', '--default-true', is_flag=True, help='Expect true by default (if no choice is made)')
@click.option('-p', '--prompt', default='Continue', help='The prompt to display')
def confirm(default_true, quiet, prompt):
    """Prompt user for a yes/no response"""
    exit(not yesno.confirm(prompt, single_key=True, default=default_true, clear=quiet))

if __name__ == "__main__":
    cli()
