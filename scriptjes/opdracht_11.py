import math


def format_print(i):
    """Pretty print value"""
    print "%.2f" % i
    print


def calculate_db(val):
    """Power log, 10 * log10(n)"""
    return 10 * math.log10(val)


def vraag_1():
    """Vraag 1"""
    print "Vraag 1"
    w_m = float(raw_input("Basisbandbreedte Wm (kHz) (ex. 10): ")) * 1e3
    delta_f = float(raw_input("Delta F (kHz) (ex. 60): ")) * 1e3
    p_norm = float(raw_input("m(t)^2/V^2p (ex. 0.65): "))
    n_0_half = float(raw_input("N0/2 (dBm/Hz) (ex. -94.3): "))
    s_in = float(raw_input("Input power (dBm) (ex. -21): "))
    times_1 = float(raw_input("IF bandwidth = ... x Carson"
                              " bandwidth (ex. 3): "))
    times_2 = float(raw_input("IF bandwidth = ... x Wm (ex. 5): "))

    # 1A
    print "1a:"

    p_rx_in = 10**((s_in - 30) / 10)
    n_0 = 10**((n_0_half - 30) / 10) * 2

    beta = delta_f / w_m
    b_t = 2 * (beta + 1) * w_m * times_1
    p_n = n_0 * b_t
    snr_in = p_rx_in / p_n

    format_print(calculate_db(snr_in))

    a_c = math.sqrt(2 * p_rx_in)
    b_1 = w_m  # Basisbandbreedte is W_m!
    snr_out = 3 * a_c**2 * beta**2 * p_norm / (2 * n_0 * b_1**3) * w_m**2

    format_print(calculate_db(snr_out))

    # 1B
    print "1b:"

    b_2 = times_2 * w_m
    snr_out = 3 * a_c**2 * beta**2 * p_norm / (2 * n_0 * b_2**3) * w_m**2

    format_print(calculate_db(snr_out))


def vraag_2():
    """Vraag 2"""
    print "Vraag 2"
    b_r = float(raw_input("Bitrate (kbit/s) (ex. 210): ")) * 1e3
    a_c = float(raw_input("s(t) = ... cos( (ex. 65): "))
    d_p = float(raw_input("2 pi fc t + ... pi d(t) (ex. 0.65): ")) * math.pi
    nth = float(raw_input("de ...de nul-null bandbreedte (ex. 2): "))
    load = float(raw_input("Belastingsweerstand (Ohm) (ex. 10): "))

    # 2A
    print "2a:"

    b_nn = 2 * b_r * nth
    format_print(b_nn * 1e-3)

    # 2B
    print "2b:"

    p_s = a_c**2 / 2
    p_r = p_s / load

    format_print(calculate_db(p_r) + 30)

    # 2C
    print "2c:"

    p_c = a_c**2 / 2 * math.cos(d_p)**2
    n_1 = p_c / p_s

    format_print(n_1 * 100)


print "Huiswerkopdracht 11"
vraag_1()
vraag_2()
