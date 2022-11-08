from rich.console import Console
import time

console = Console()

console.rule("[bold red] Testing status")

with console.status("Let me think...", spinner="monkey"):
	for sampleIndex in range(0, 5):
		print (sampleIndex)
		time.sleep(5)

console.rule("Stopped thinking")
