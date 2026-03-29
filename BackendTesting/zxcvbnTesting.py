from zxcvbn import zxcvbn

# Returns string
def password_test(password):
    r = zxcvbn("te$t12343😀32")
    print("time to crack ", r["calc_time"], " | guesses ", r["guesses"], " | Score: ", r["score"])
    return "time to crack ", r["calc_time"], " | guesses ", r["guesses"], " | Score: ", r["score"]