import os
import sys

import click
import requests
import yaml


TEMPLATE = \
b'''from coiiot_sdk import (
    user_logs,
    context,
)


logger = user_logs.get_logger()
ctx = context.current()

logger.info(f'rule_name={ctx.rule.name}')
logger.info(f'tag_full_name={ctx.tag.full_name}')
logger.info(f'value={ctx.msg.value}')
'''


class Config(object):

    RULES_FOLDER_NAME = 'rules'
    CFG_FILE_NAME = '.config.yml'
    client_id: int
    api_key: str
    addr: str
    ready: bool = False

    def __init__(self, path=None):
        self.path = os.path.abspath(path or '.')

        if os.path.exists(self.get_config_path()):
            self.read_config()
            self.ready = True

    def get_config_path(self) -> str:
        return os.path.join(self.path, self.CFG_FILE_NAME)

    def get_rules_path(self) -> str:
        return os.path.join(self.path, self.RULES_FOLDER_NAME)

    def get_rule_path(self, name: str) -> str:
        return os.path.join(self.get_rules_path(), f'{ name }.py')

    def write_config(self):
        with open(os.path.join(self.path, self.CFG_FILE_NAME), mode='w') as f:
            yaml.dump({
                "client_id": self.client_id,
                "api_key": self.api_key,
                "addr": self.addr,
            }, f)

    def read_config(self):
        with open(os.path.join(self.path, self.CFG_FILE_NAME), mode='r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
            self.client_id = data['client_id']
            self.api_key = data['api_key']
            self.addr = data['addr']


@click.group()
@click.option('--path', default='.')
@click.pass_context
def cli(ctx, path):
    ctx.obj = Config(path)


@click.group(name='rules')
@click.pass_context
def rules(ctx):
    pass


@click.command(name="new")
@click.argument('name', type=click.STRING)
@click.pass_context
def new_rule(ctx, name):
    if not ctx.obj.ready:
        click.echo("Project was not inited! Aborting ...")
        sys.exit(1)

    path = ctx.obj.get_rule_path(name)
    if os.path.exists(path):
        click.echo(f"Rule in path '{ path }' already exists! Aborting ...")
        sys.exit(1)

    click.echo(f"Create new rule with name = '{ name }' in path '{ path }'")
    with open(path, mode='wb') as f:
        f.write(TEMPLATE)

    click.echo(f"New rule was successfully created in path '{ path }'")

    resp = requests.post(
        f"{ctx.obj.addr}/v1/rules",
        headers={"X-Api-Key": ctx.obj.api_key},
        json={
            "name": name,
            "code": TEMPLATE,
            "enabled": True,
            "lang_id": 0,
            "type": 1,
            "client_id": ctx.obj.client_id,
        },
    )
    if resp.status_code != 200:
        os.remove(path)
        click.echo(resp.status_code)
        click.echo(resp.text)
        click.echo("Failed to create new rule via HTTP API! Aborting ...")
        sys.exit(1)

    click.echo(f"New rule was successfully created via HTTP API")


@click.command(name="commit")
@click.argument('name', type=click.STRING)
@click.pass_context
def commit_rule(ctx, name):
    if not ctx.obj.ready:
        click.echo("Project was not inited! Aborting ...")
        sys.exit(1)

    path = ctx.obj.get_rule_path(name)
    if not os.path.exists(path):
        click.echo(f"Rule in path '{ path }' is not exists! Aborting ...")
        sys.exit(1)

    resp = requests.get(
        f"{ctx.obj.addr}/v1/clients/{ctx.obj.client_id}/rules",
        headers={"X-Api-Key": ctx.obj.api_key},
        params={"name": name}
    )
    if resp.status_code != 200:
        click.echo(resp.status_code)
        click.echo(resp.text)
        click.echo("Failed to get rule info from HTTP API! Aborting ...")
        sys.exit(1)

    data = resp.json()
    if len(data['items']) == 0:
        click.echo("Rule in HTTP API not found! Aborting ...")
        sys.exit(1)

    rule_id = data['items'][0]['id']
    with open(path, 'r') as f:
        new_code = f.read()

    resp = requests.patch(
        f"{ctx.obj.addr}/v1/rules/{rule_id}",
        headers={"X-Api-Key": ctx.obj.api_key},
        json={"code": new_code}
    )
    if resp.status_code != 200:
        click.echo(resp.status_code)
        click.echo(resp.text)
        click.echo("Failed to update rule code via HTTP API! Aborting ...")
        sys.exit(1)

    click.echo(f"Rule was successfully committed via HTTP API")


@click.command(name="fetch")
@click.argument('name', type=click.STRING)
@click.pass_context
def fetch_rule(ctx, name):
    if not ctx.obj.ready:
        click.echo("Project was not inited! Aborting ...")
        sys.exit(1)

    click.echo("Fetching rule")
    resp = requests.get(
        f"{ctx.obj.addr}/v1/clients/{ctx.obj.client_id}/rules",
        headers={"X-Api-Key": ctx.obj.api_key},
        params={"name": name}
    )
    if resp.status_code != 200:
        click.echo(resp.status_code)
        click.echo(resp.text)
        click.echo("Failed to fetch rule via HTTP API! Aborting ...")
        sys.exit(1)

    data = resp.json()
    if len(data['items']) == 0:
        click.echo("Rule in HTTP API not found! Aborting ...")
        sys.exit(1)

    code = data['items'][0]['code']
    path = ctx.obj.get_rule_path(name)
    with open(path, 'w') as f:
        f.write(code)

    click.echo(f"Successfully fetched rule via HTTP API")


@click.command(name="init")
@click.option('--key', help='Api Key to communicate with CoIIoT platform', required=True)
@click.option('--addr', help='CoIIoT platform address', required=True)
@click.pass_context
def init(ctx, key, addr):
    if ctx.obj.ready:
        click.echo("Project was already inited! Aborting ...")
        sys.exit(1)

    click.echo("Init project sdk")

    click.echo("Get current client")
    resp = requests.get(f"{addr}/v1/clients/current", headers={"X-Api-Key": key})
    if resp.status_code != 200:
        click.echo(resp.text)
        click.echo("Failed to get current client info from HTTP API! Aborting ...")
        sys.exit(1)

    client = resp.json()
    click.echo(f"Current client has id = { client['id'] }")

    click.echo(f"Ensure that project path '{ ctx.obj.path }' exists")
    os.makedirs(ctx.obj.path, exist_ok=True)

    click.echo(f"Creating folder for rules '{ ctx.obj.get_rules_path() }'")
    os.makedirs(ctx.obj.get_rules_path(), exist_ok=True)

    click.echo(f"Creating config file in path { ctx.obj.get_config_path() }")
    ctx.obj.client_id = client['id']
    ctx.obj.api_key = key
    ctx.obj.addr = addr
    ctx.obj.write_config()

    click.echo("Project sdk successfully inited")


rules.add_command(new_rule)
rules.add_command(commit_rule)
rules.add_command(fetch_rule)
cli.add_command(rules)
cli.add_command(init)


if __name__ == '__main__':
    cli()
