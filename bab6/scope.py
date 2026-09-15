x = 10 # variable global

def fungsi_a():
    x = 99 
    print("di dalam fungsi_a, x =", x)

def fungsi_b():
    print("di dalam fungsi_b, x =", x)

fungsi_a()
fungsi_b()
print("di luar fungsi, x =", x)