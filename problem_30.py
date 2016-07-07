from timeit import default_timer as timer

def digit_powers(exponent):
    def power(k):
        return int(k) ** exponent
    if exponent <= 1:
        return "The exponent must be at least 2."
    else:
        total_sum = 0
        upper_bound = (exponent + 1) * (9 ** exponent)
        for number in range(10, upper_bound + 1):
            digits = [x for x in str(number)]
            if number == sum(map(power, digits)):
                total_sum += number
        return total_sum

start = timer()
ans = digit_powers(5)
elapsed_time = (timer() - start) * 1000 # s --> ms

print "Found %d in %r ms." % (ans, elapsed_time)