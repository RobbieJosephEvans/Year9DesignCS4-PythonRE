#CAUSTION - DO NOT USE WHILE LOOPS TO CONTROL INPUTS WITH GUI PROGRAMS

print("******************************")
print("Counted Loops: For")

print("0")
print("1")
print("2")
print("3")


#When we think of a for loop I want think about
# Count: The variable that holds the current count
# Check: The check that is done each time the loop runs
# Change: The change appled to the count each time the loop runs

#for <count var> in rance (<initial value>, <check value>, <change>):


print("*****************************")
for i in range (0,4,1):
	print(i)

print("******************************")
#Change the loop parameters so it prints -44 to 136 inclusive

for i in range(-44,137,1):
	print()
	if (i % 2 == 0):
		print(str(i)+" is even")
	else:
		print(str(i)+" is odd")
