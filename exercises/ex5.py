name = 'Zed A. Shaw'
age = 35 # prolly a lie
height = 74  * 2.54# please do not use freedom units
weight = round(180 / 2.2046) # I wish
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total:.2f}.")

