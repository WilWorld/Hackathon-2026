from zxcvbn import zxcvbn
from datetime import timedelta

# Returns string
def password_test(password):
    if len(password) > 72:
        return ["Password exceeds 72 characters", "For stats, have a password under 72 characters"]
    
    r = zxcvbn(password)
    time = "Time: " + format_time(r["calc_time"])
    guess = "Guesses: " + format_guesses(r["guesses"])
    score = "Score: " + format_score(r["score"])

    return [time, guess, score]

# Formats time in a meaningful way
def format_time(td):
    seconds = td.total_seconds()
    if seconds < 1e-6:   # smaller than one microsecond -> nanosecond
        return f"{seconds * 1e9:.0f} ns"
    elif seconds < 1e-3: # smaller than one milisecond  -> microsecond
        return f"{seconds * 1e6:.0f} µs"
    elif seconds < 1:    # smaller than one second      -> milisecond
        return f"{seconds * 1e3:.0f} ms"
    else:                # one second or bigger         -> second
        return f"{seconds:.0f} s"       

# Formats guesses in a meaningful way 
def format_guesses(guesses):
    scales = [
        (10**303, "centillion"), 
        (10**300, "novemnonagintillion"), 
        (10**297, "octononagintillion"), 
        (10**294, "septennonagintillion"), 
        (10**291, "sexnonagintillion"), 
        (10**288, "quindecennonagintillion"), 
        (10**285, "quattuordecennonagintillion"), 
        (10**282, "tredecennonagintillion"), 
        (10**279, "duodecennonagintillion"), 
        (10**276, "undecennonagintillion"), 
        (10**273, "decennonagintillion"), 
        (10**270, "nonagintillion"), 
        (10**267, "octogintillion"), 
        (10**264, "septuagintillion"), 
        (10**261, "sexagintillion"), 
        (10**258, "quinquagintillion"), 
        (10**255, "quadragintillion"), 
        (10**252, "trigintillion"),
        (10**63, "vigintillion"),
        (10**60, "novemdecillion"),
        (10**57, "octodecillion"),
        (10**54, "septendecillion"),
        (10**51, "sexdecillion"),
        (10**48, "quindecillion"),
        (10**45, "quattuordecillion"),
        (10**42, "tredecillion"),
        (10**39, "duodecillion"),
        (10**36, "undecillion"),
        (10**33, "decillion"),
        (10**30, "nonillion"),
        (10**27, "octillion"),
        (10**24, "septillion"),
        (10**21, "sextillion"),
        (10**18, "quintillion"),
        (10**15, "quadrillion"),
        (10**12, "trillion"),
        (10**9,  "billion"),
        (10**6,  "million"),    
        (10**3,  "thousand"),
    ]

    for value, name in scales:
        if guesses >= value:
            return f"{guesses / value:.0f} {name}"

    return str(guesses)

# Formats the score in a meaningful way
def format_score(score):
    if score == 0:
        return f"{score} [very weak]"
    if score == 1:
        return f"{score} [weak]"
    if score == 2:
        return f"{score} [fair]"
    if score == 3:
        return f"{score} [strong]"
    if score == 4:
        return f"{score} [very strong]"