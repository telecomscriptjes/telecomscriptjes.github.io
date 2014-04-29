def format_print(i):
	print "%.2f" % i

print "Huiswerkopdracht 8"

range_lower = int(raw_input("Afstemband - ondergrens [kHz] (ex. 13200) "))
range_upper = int(raw_input("Afstemband - bovengrens [kHz] (ex. 22300) "))


high_low = raw_input("LO hoger/lager dan Afstemband? (ex. hoger) ")
if high_low != "lager" and high_low != "hoger":
	print "Verkeerde invoer, vul hoger of lager in"
	high_low = raw_input("LO hoger/lager dan Afstemband? (ex. hoger) ")

if_freq = int(raw_input("IF frequentie [kHz] (ex. 2350) "))

# 1A
print "1a:"
if high_low == "hoger":
	low = range_lower + if_freq
	high = range_upper + if_freq
else:
	low = range_lower - if_freq
	high = range_upper - if_freq

format_print(low)
format_print(high)

# 1B
print "1b:"
if high_low == "hoger":
	low = range_lower + 2*if_freq
	high = range_upper + 2*if_freq
else:
	low = range_lower - 2*if_freq
	high = range_upper - 2*if_freq

format_print(low)
format_print(high)

# 1C
print "1c:"
minimal_if_freq = (range_upper - range_lower) / 2.0
format_print(minimal_if_freq)


# 1D
print "1d:"
print "Het filteren van spiegefrequenties dient te gebeuren voor de mixer"
print "F"