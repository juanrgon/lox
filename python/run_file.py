from run import run


def run_file(path: str):
    with open(path) as file:
        run(file.read())
