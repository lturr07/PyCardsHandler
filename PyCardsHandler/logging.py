class logs():
    log_start = 0
    log_end = 1
    log_success = 2
    log_fail = 3
    log_input = 4
    log_warning = 5
    log_info = 6
    log_comment = 7
    log_debug = 8

_log_styles = [
    ["<", "\033[94m"],  # Start
    [">", "\033[94m"],  # End
    ["+", "\033[92m"],  # Success
    ["!", "\033[91m"],  # Fail
    ["?", "\033[95m"],  # Input
    ["!", "\033[93m"],  # Warning
    ["#", "\033[94m"],  # Info
    ["#", "\033[95m"],  # Comment
    ["~", "\033[96m"]   # Debug
]

def log(logtype: int, *msg, sep: str = " ", end: str = "\n") -> None:
    style = _log_styles[logtype]
    _log(style[0], style[1], sep.join(msg), end=end)

def _log(logtype: str, colour: str, *msg, sep: str = " ", end: str = "\n") -> None:
    a = "\033[1m" + colour + "[" + logtype + "]" + "\033[0m"
    print(a, *msg, sep=sep, end=end)

def ask(prompt: str, *opt: str, onwrong: str = "Please choose from:") -> int:
    while True:
        log(4, prompt.strip() + " ", end="")
        inp = input().lower()
        for i, option in enumerate(opt):
            if inp == option.lower():
                return i
        log(3, onwrong.strip(), *opt)

if __name__ == "__main__":
    log(logs.log_fail, "This is a module, do not run directly")