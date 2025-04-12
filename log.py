import inspect
import os
import colorama
import time

log_format = "{time} | {level} | {filename_only}: {line} - {function} | {string}"
time_format = "{year}-{month}-{day} {hour}:{minute}:{sec}"

colorama.init(True)


class LogLevel:
    DEBUG = "Debug"
    TIP = "Tip"
    INFO = "Info"
    WARRING = "Warning"
    ERROR = "Error"
    CRASH = "Crash"
    FATAL_ERROR = "Fatal error"


def log(string, log_level=LogLevel.INFO):
    now_time = time.localtime()
    time_str = time_format.format(year=now_time.tm_year,
                                  month=now_time.tm_mon,
                                  day=now_time.tm_mday,
                                  hour=now_time.tm_hour,
                                  minute=now_time.tm_min,
                                  sec=now_time.tm_sec)

    frame = inspect.currentframe()
    caller_frame = inspect.stack()[1]

    filename_full = caller_frame.filename
    filename_only = os.path.basename(filename_full)

    line = frame.f_back.f_lineno
    func = caller_frame.function

    message = log_format.format(filename_full=filename_full,
                                filename_only=filename_only,
                                line=line,
                                string=string,
                                function=func,
                                level=log_level,
                                time=time_str)

    if log_level == LogLevel.FATAL_ERROR or log_level == LogLevel.CRASH:
        print(colorama.Back.RED + message)
    elif log_level == LogLevel.ERROR or log_level == LogLevel.WARRING:
        print(colorama.Back.YELLOW + message)
    elif log_level == LogLevel.INFO:
        print(message)
    elif log_level == LogLevel.TIP:
        print(colorama.Fore.BLUE + message)
    else:
        print(message)

