from lib.crossroads import Crossroads
from cli.cli import CLI

crossroads = Crossroads()
cli = CLI(crossroads)
cli.run()
