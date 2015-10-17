print("python_intro.py")
if 3>2:
	print("python_intro.py")
if 5>2:
	print("5 is indeed greater than 2")
else:
	print("5 is not greater than 2")

name = "Elektra"
if name == "Ola":
	print("Hey Ola!")
elif name == "Elektra":
	print("Hey Elektra")
else:
	print("Hey anonymous")

def hi(name):
	print("Hi " + name + "!")
girls = ["Rachel", "Monica", "Elena"]
for name in girls:
	hi(name)
	print("Next girl")
	
