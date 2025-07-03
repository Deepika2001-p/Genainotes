import numpy as np

# counts
rain_low = 5
no_rain_low = 30

rain_high = 25
no_rain_high = 5

# totals
total_rain = rain_low + rain_high
total_no_rain = no_rain_low + no_rain_high

# proportions
perc_rain_low = rain_low / total_rain
perc_rain_high = rain_high / total_rain

perc_no_rain_low = no_rain_low / total_no_rain
perc_no_rain_high = no_rain_high / total_no_rain

# WOE (Weight of Evidence)
woe_low = np.log(perc_rain_low / perc_no_rain_low)
woe_high = np.log(perc_rain_high / perc_no_rain_high)

# IV for each group
iv_low = (perc_rain_low - perc_no_rain_low) * woe_low
iv_high = (perc_rain_high - perc_no_rain_high) * woe_high

# Total IV
iv_total = iv_low + iv_high

print(f"WOE Low Humidity: {woe_low:.2f}")
print(f"WOE High Humidity: {woe_high:.2f}")
print(f"IV Low Humidity: {iv_low:.2f}")
print(f"IV High Humidity: {iv_high:.2f}")
print(f"Total IV: {iv_total:.2f}")
