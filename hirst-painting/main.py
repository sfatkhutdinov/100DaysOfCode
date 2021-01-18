import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract("image.jpg", 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)

print(rgb)
