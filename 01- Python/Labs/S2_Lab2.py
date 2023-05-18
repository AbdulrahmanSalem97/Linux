f1 = open("File.txt","x")

name = input("Please enter your name\n")
year = input("Please enter your date of birth\n")
tier = input("Please enter your tier\n")

f1.write(name)
f1.write("\n")
f1.write(year)

f1.write(tier)


f1.close()