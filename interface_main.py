def line(tam = 42):
    return("-" * tam)
def print_line (tam = 42):
    print(line(tam))

def spotlight(txt, tam = 42):
    return (f"#{line(tam)}#\n{txt.center(tam)}\n#{line(tam)}#")
def print_spotlight(txt, tam = 42):
    print(spotlight(txt, tam))




