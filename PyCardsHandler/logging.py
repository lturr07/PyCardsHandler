class logs():
    log_debug = -1
    log_start = 0
    log_end = 1
    log_success = 2
    log_fail = 3
    log_input = 4
    log_warning = 5
    log_info = 6
    log_comment = 7

def log(logtype: int, *msg, end = "\n") -> None:
    match logtype:
        case 0:
            _log("<", "\033[94m", *msg, end=end)
        case 1:
            _log(">", "\033[94m", *msg, end=end)
        case 2:
            _log("+", "\033[92m", *msg, end=end)
        case 3:
            _log("!", "\033[91m", *msg, end=end)
        case 4:
            _log("?", "\033[95m", *msg, end=end)
        case 5:
            _log("!", "\033[93m", *msg, end=end)
        case 6:
            _log("#", "\033[94m", *msg, end=end)
        case 7:
            _log("#", "\033[95m", *msg, end=end)
        case -1:
            _log("~", "\033[96m", *msg, end=end)

def _log(logtype: str, colour: str, *msg, end = "\n") -> None:
    a = "\033[1m" + colour + "[" + logtype + "]" + "\033[0m"
    print(a, *msg, end=end)

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