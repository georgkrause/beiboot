import click
from prompt_toolkit import print_formatted_text

from beiboot.configuration import ClientConfiguration

from cli.cluster import (
    create_cluster,
    delete_cluster,
    list_clusters,
    connect,
    inspect,
    disconnect,
)
from cli.install import install, uninstall


@click.group()
@click.option(
    "--kubeconfig",
    help="Path to the kubeconfig file to use instead of loading the default",
)
@click.option(
    "--context",
    help="Context of the kubeconfig file to use instead of 'default'",
)
@click.pass_context
def cli(ctx, kubeconfig, context):
    ctx.ensure_object(dict)
    ctx.obj["config"] = ClientConfiguration(
        kube_config_file=kubeconfig, kube_context=context
    )


@click.command()
@click.pass_context
def version(ctx):
    from beiboot.configuration import __VERSION__

    print_formatted_text("Beiboot version: " + __VERSION__)


cli.add_command(version)


@click.group("cluster")
@click.pass_context
def cluster(ctx):
    pass


cluster.add_command(create_cluster)  # type: ignore
cluster.add_command(delete_cluster)  # type: ignore
cluster.add_command(list_clusters)  # type: ignore
cluster.add_command(connect)  # type: ignore
cluster.add_command(disconnect)  # type: ignore
cluster.add_command(inspect)  # type: ignore


cli.add_command(cluster)

cli.add_command(install)
cli.add_command(uninstall)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
