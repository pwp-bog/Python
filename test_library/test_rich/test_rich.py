from rich import print
from rich.panel import Panel
from rich.text import Text


print(Panel(Text("Fuck you", justify="center")))


text = "[bold red]Hello[/] world bitch"
print(text)
print("[italic blue]World")
print("[uu green]!!!")
print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")
print("Hello[red] world")
print(":red_heart-text:")

#from rich.text import Text
#from rich.panel import Panel
text = Panel(Text("bebra", tab_size=8))
print(text)
