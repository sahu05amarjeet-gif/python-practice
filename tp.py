import pathlib
desktop = pathlib.Path("/home/amar/Documents")
print(list(desktop.rglob("*")))