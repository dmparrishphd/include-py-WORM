def include(file, there=globals(), here=globals()):
    with open(file) as f:
        exec(f.read(), there, here)
