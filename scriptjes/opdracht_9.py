import math

def format_print(i):
	print "%.2f" % i
	print

print "Huiswerkopdracht 9"

B = 400 #Hz

mu = float(raw_input("Modulation index mu (ex. 0.3): "))

x_max = float(raw_input("x_max = -x_min (ex. 0.9): "))
x_min = -x_max

e_x_2 = float(raw_input("E[x(t)^2] (ex. 0.4): "))

A_c = float(raw_input("Amplitude ongemoduleerde draaggolf (ex. 100): "))
Z_ant = float(raw_input("Stralingsweerstand antenne (ex. 90): "))

#1A
print "1a:"
m = mu * (x_max - x_min) / 2.0 * 100.0
format_print(m)

#1B
print "1b:"
P_avg = (A_c**2) / (2*Z_ant) * (1 + mu**2 * e_x_2)
P_avg_db = 10*math.log10(P_avg)
format_print(P_avg_db)

#1C
print "1c:"
P_pep = (A_c**2) / (2*Z_ant) * (1 + mu * x_max)**2
P_pep_db = 10*math.log10(P_pep)
format_print(P_pep_db)

#1D
print "1d:"
E = (mu**2 * e_x_2) / (1 + mu**2 * e_x_2) * 100.0
format_print(E)

#1E
print "1e:"
Psb = A_c**2 / (Z_ant * 2) * mu**2 * e_x_2
Psb_db = 10*math.log10(1000 * Psb / 800)
format_print(Psb_db)

modulation = raw_input("Modulation type LSSB/USSB (ex. USSB): ")

if modulation != "USSB" and modulation != "LSSB":
	print "Verkeerde invoer, vul USSB of LSSB in"
	modulation = raw_input("Modulation type LSSB/USSB (ex. USSB): ")

A_m = float(raw_input("Am (ex. 2): "))
B_m = float(raw_input("Bm (ex. 3.5): "))
A_c = float(raw_input("Ac (ex. 230): "))
R_l = float(raw_input("Belastingsweerstand (ex. 100): "))

#2A
print "2a:"
if modulation == "LSSB":
	print "st = Ac Am cos(2 pi (fc - fm)t) + Ac Bm sin(2 pi (fc - fm)t)"
else:
	print "st = Ac Am cos(2 pi (fc + fm)t) + Ac Bm sin(2 pi (fc + fm)t)"
print

#2B
print "2b:"
V_rms = math.sqrt( (A_m * A_c / math.sqrt(2))**2 + (B_m * A_c / math.sqrt(2))**2 )
format_print(V_rms)

#2C
print "2c:"
maximum = A_c * (A_m + B_m)
format_print(maximum)

#2D
print "2d:"
P_avg = ((A_m * A_c / math.sqrt(2))**2 + (B_m * A_c / math.sqrt(2))**2) / R_l
P_avg_db = 10*math.log10(P_avg)
format_print(P_avg_db)

P_pep = 0.5 * maximum**2 / R_l
P_pep_db = 10 * math.log10(P_pep)
format_print(P_pep_db)

