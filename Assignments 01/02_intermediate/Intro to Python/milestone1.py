# Get user input
earth_weight = float(input("Enter a weight on Earth: "))

# Mars gravity factor
mars_gravity = 0.378

# Calculate weight on Mars
mars_weight = round(earth_weight * mars_gravity, 2)

# Print result
print("The equivalent on Mars:", mars_weight)
