from zxcvbn import zxcvbn

# Returns string
def password_test(password):
    if len(password) > 72:
        return ["Password exceeds 72 characters", "For stats, have a password under 72 characters"]
    
    r = zxcvbn(password)
    time = "Time to crack: " + str(r["calc_time"])
    guess = "Number of guesses: " + str(r["guesses"])
    score = "Score: " + str(r["score"])

    return [time, guess, score]
