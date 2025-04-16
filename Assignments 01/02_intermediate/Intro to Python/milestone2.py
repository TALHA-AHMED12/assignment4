# Get user input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Gravity constants
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get gravity for chosen planet
gravity = gravity_factors[planet]

# Calculate planetary weight
planetary_weight = round(earth_weight * gravity, 2)

# Print result
print(f"The equivalent weight on {planet}: {planetary_weight}")
