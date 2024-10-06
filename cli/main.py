from lib.crossroads import Crossroads
from cli.cli import CLI

crossroads = Crossroads(use_dotenv=True)
cli = CLI(crossroads)
cli.run()
