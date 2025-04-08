import inspect
import os

def log(string):
    frame = inspect.currentframe()
    filename = os.path.basename(frame.f_code.co_filename)
    line = frame.f_back.f_lineno
    print(f"{filename}:{line} - {string}")
log("log")