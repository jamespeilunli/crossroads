from rich.markdown import Heading, Markdown
from rich import box
from rich.panel import Panel
from rich.text import Text

class MyHeading(Heading):
    """
    see https://rich.readthedocs.io/en/latest/_modules/rich/markdown.html?highlight=Heading#
    i slightly modified it to left-justify headings instead of centering
    """

    def __rich_console__(self, console, options):
        text = self.text
        text.justify = "left"
        if self.tag == "h1":
            yield Panel(
                text,
                box=box.HEAVY,
                style="markdown.h1.border",
            )
        else:
            if self.tag == "h2":
                yield Text("")
            yield text

Markdown.elements['heading_open'] = MyHeading
