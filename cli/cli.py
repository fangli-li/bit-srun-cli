import click
from .command import cmd


@click.group()
# @click.option('--verbose', is_flag=True, help='打印debug信息')
def cli():
    """
    北理工校园网登录命令行工具\n
    项目地址 https://github.com/fangli-li/bit-srun-cli
    """
    pass


@click.command('login', short_help='登录校园网')
def login():
    click.echo('开始登录...')
    cmd.login()


@click.command('logout', short_help='注销校园网')
def logout():
    click.echo('开始注销...')
    cmd.logout()
    pass


@click.command('config', short_help='配置用户名密码')
def config():
    click.echo('开始进行配置...')
    cmd.config()

@click.command('info', short_help='查看网络状态')
def info():
    click.echo("开始查询信息...")
    cmd.info()

cli.add_command(login)
cli.add_command(config)
cli.add_command(logout)
cli.add_command(info)

if __name__ == '__main__':
    cli()
