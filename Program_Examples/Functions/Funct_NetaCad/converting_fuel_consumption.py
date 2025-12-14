# The constant for converting L/100km to MPG (and vice versa) is ~235.21458.
CONVERSION_FACTOR = 235.214583


def liters_100km_to_miles_gallon(liters):
    # MPG = CONVERSION_FACTOR / (L/100km)
    if liters == 0:
        return 0.0
    return CONVERSION_FACTOR / liters


def miles_gallon_to_liters_100km(miles):
    # L/100km = CONVERSION_FACTOR / MPG
    if miles == 0:
        # A vehicle with 0 MPG means it uses an infinite amount of fuel,
        # which is often represented by a large number or 0 L/100km in a practical context
        return 0.0
    return CONVERSION_FACTOR / miles


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757
