name = 'Zed A. Shaw'
age = 35 #Not A lie
height = 74 #Inches
wieght = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#Conversion to metric system
heightMetric = height * 2.54
wieghtMetric = wieght * 0.453592
#output
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {wieght} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes}  eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

#This line is tricky, try to get it exactly right
total = age + height + wieght
print(f"If I add {age}, {height}, and {wieght} I get {total}.")

#Metic output
print(f"He's {heightMetric} centimeters tall.")
print(f"He's {wieghtMetric} kilograms heavy.")
