from zxcvbn import zxcvbn


r = zxcvbn("te$t12343😀32")
print("time to crack ", r["calc_time"], " | guesses ", r["guesses"], " | Score: ", r["score"])