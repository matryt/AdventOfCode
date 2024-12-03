def read_file(path):
    with open(path) as f:
        return "\n".join(f.readlines())