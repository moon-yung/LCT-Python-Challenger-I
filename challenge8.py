day = int(input("Enter number of days: "))
hours = day * 24
minutes = day * 1440
seconds = day * 86400

print(f'''
	In {day} day/s there are...
	{hours} total hours
	{minutes} total minutes
	{seconds} total seconds
	''')