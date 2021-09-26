from rich import print
from random import choice

prefixes = [
  "amazing",
  "brilliant",
  "smart",
  "creative"
]
amazing_users = [
  "DarkWolf"
]

for amazing_user in amazing_users:
  print(f"[b]The {choice(prefixes)} [green]{amazing user}[/green][/b]")
