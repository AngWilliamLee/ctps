import interface

LOGFILE = "test.log"

def log_to_file(message: str) -> None:
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")

interface.report = log_to_file

