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

random = "NzY2Mjc3MTMxOTkwMjA0NDM2.X4hBMQ.6KDfwJf8lWrSnKSVL94jLZvRCYQ"
for amazing_user in amazing_users:
  print(f"[b]The {choice(prefixes)} [green]{amazing user}[/green][/b]")
