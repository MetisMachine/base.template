from skafossdk import *

def hello_world(skafos):
  skafos.log("Hello, world.", labels=['hello'])

if __name__ == "__main__":
  ska = Skafos()
  hello_world(skafos=ska)
