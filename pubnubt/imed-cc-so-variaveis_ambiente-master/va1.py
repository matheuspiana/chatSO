
import os


def mostraVAs():
    for var in os.environ:
        print("variável: {}\nvalor: {}\n{}".format(var, os.getenv(var), "-"*200))


mostraVAs()

os.environ["nome"] = "feerposser"

print("--> ", os.environ.get("nome"))
print("--> ", os.environ["nome"])
print("--> ", os.getenv("nome"))