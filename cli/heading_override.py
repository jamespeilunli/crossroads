from rich.markdown import Heading, Markdown
from rich import box
from rich.console import Console, ConsoleOptions
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

class MyHeading(Heading):
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) :
        text = self.text
        text.justify = "left"
        if self.tag == "h1":
            # Draw a border around h1s
            yield Panel(
                text,
                box=box.HEAVY,
                style="markdown.h1.border",
            )
        else:
            # Styled text for h2 and beyond
            if self.tag == "h2":
                yield Text("")
            yield text

Markdown.elements['heading_open'] = MyHeading


