handlers = []

modules = ["index"]

for module in modules:
    handler = __import__("src.handlers." + module, fromlist="src.handlers")
    handlers.append(handler.handler)
