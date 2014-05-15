import math


def format_print(i):
    """Pretty print value"""
    print "%.2f" % i
    print


def db(n):
    """Power log, 10 * log10(n)"""
    return 10 * math.log10(n)


def vraag_1():
    """Vraag 1"""
    print "Vraag 1"
    f_audio = 15e3
    x_max = 1
    f_carrier = float(raw_input("Draaggolffrequentie (MHz) (ex. 92): ")) * 1e6
    multiplication = float(raw_input("Vermenigvuldiging (ex. 4): "))
    f_mod = float(raw_input("Modulator frequentie (MHZ) (ex. 5): ")) * 1e6
    hoger_lager = raw_input("f0 hoger/lager dan fi (ex. hoger): ")

    if hoger_lager != "hoger" and hoger_lager != "lager":
        print "Verkeerde invoer, vul hoger of lager in"
        hoger_lager = raw_input("f0 hoger/lager dan fi (ex. hoger): ")

    d_p = float(raw_input("Piek-fasedeviatie (rad) (ex. 0.3): "))

    # 1A
    print "1a:"

    f_band = f_carrier / multiplication

    f_shift1 = f_band - f_mod
    f_shift2 = f_band + f_mod

    f_osc1 = f_shift1
    f_osc2 = f_shift2

    if hoger_lager == "lager":
        if f_osc1 < f_band:
            f_osc = f_osc1
        elif f_osc2 < f_band:
            f_osc = f_osc2
        else:
            f_osc = -1
            print "1a fosc is niet juist, er ging iets mis"
    else:
        if f_osc1 > f_band:
            f_osc = f_osc1
        elif f_osc2 > f_band:
            f_osc = f_osc2
        else:
            f_osc = -1
            print "1a fosc is niet juist, er ging iets mis"

    format_print(f_band * 1e-3)
    format_print(f_osc * 1e-3)

    # 1B
    print "1b:"
    max_phase = math.pi / multiplication
    d_p_max = max_phase / x_max

    format_print(d_p_max)

    # 1C
    print "1c:"
    beta = d_p * x_max
    bw_t = 2 * (beta + 1) * f_audio

    format_print(bw_t*1e-3)


def vraag_2():
    """Vraag 2"""
    print "Vraag 2"
    print "Deel 1:"
    a_c = float(raw_input("Ac (ex. 130): "))
    b = float(raw_input("B (ex. 2.5): "))
    f_m1 = float(raw_input("fm (kHz) (ex. 32): ")) * 1e3
    d_p1 = float(raw_input("Dp (ex. 0.45): "))
    d_f1 = float(raw_input("Df (kHz/V) (ex. 60): ")) * 1e3

    print "Deel 2:"
    d_f2 = float(raw_input("Df (kHz/V) (ex. 0.3): ")) * 1e3
    f_m2 = float(raw_input("fm (kHz) (ex. 5): ")) * 1e3
    n = float(raw_input("n (ex. 32): "))
    delta_f = float(raw_input("Delta F (kHz) (ex. 15): ")) * 1e3

    # 2A
    print "2a:"
    a_m = b / d_p1
    format_print(a_m)

    # 2B
    print "2b:"
    a_m = b * f_m1 / d_f1
    print 'Antwoord klopt, maar volgens mij zit er een factor 2*pi fout'
    format_print(a_m)

    # 2C
    print "2c:"

    betas = [2.40, 3.83, 5.14, 6.38, 7.59, 8.77, 9.93]
    beta_1 = betas[int(n)]

    a_m = beta_1 * f_m2 / d_f2
    print 'Antwoord klopt, maar volgens mij zit er een factor 2*pi fout'
    format_print(a_m)

    # 2D
    print "2d:"
    beta_2 = delta_f / f_m2
    bw_t = 2 * (beta_2 + 1) * f_m2
    format_print(beta_2)
    format_print(bw_t * 1e-3)


def vraag_3():
    """Vraag 3"""
    print "Vraag 3"
    n_0_half = float(raw_input("N0 / 2 (ex. 3.5e-9): "))
    x_m_power = float(raw_input("[m^2(t)] (ex. 0.20): "))
    x_m_avg = float(raw_input("[m(t)] (ex. 0): "))    
    bw_x = float(raw_input("Wm (kHz) (ex. 5): ")) * 1e3
    mu = float(raw_input("Modulatie-index mu (ex. 0.45): "))
    p_no_mod = float(raw_input("P_no_mod (dBm) (ex. 16): "))

    # 3A
    print "3a:"
    p_no_mod = 10**(p_no_mod / 10) / 1e3
    n_0 = n_0_half * 2

    bw_sig_mod = 2 * bw_x
    n_sig_mod = bw_sig_mod * n_0
    p_sig_mod = p_no_mod * (1 + mu**2 * x_m_power)
    snr_in = p_sig_mod / n_sig_mod

    # Signal restored:
    # carrier removed and effect of half power by carrier nullified
    # Half power by carrier removal can also be interpreted as addition of
    # amplitudes by demodulation
    p_sig_demod = (p_sig_mod - p_no_mod) * 2
    snr_out = p_sig_demod / n_sig_mod

    format_print(db(snr_in))
    format_print(db(snr_out))

    # 3B
    print "3b:"
    # There is no difference using DSB-SC modulation, as the signal is in a
    # same way demodulated
    format_print(db(snr_out))

    # 3C
    print "3c:"

    # LSSD uses only the lower side bands, this means that the power received
    # is decreased by a factor two. Equivalently, only the carrier power is
    # removed, but there is no addition of ampltides.
    p_sig_demod = p_sig_mod - p_no_mod
    snr_out = p_sig_demod/n_sig_mod

    format_print(db(snr_out))

print "Huiswerkopdracht 10"
vraag_1()
vraag_2()
vraag_3()
