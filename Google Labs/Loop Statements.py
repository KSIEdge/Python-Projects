#1
# Iterative statement using `for`, `range()`, and a loop variable of `i`
# Display "Connection could not be established." three times
for i in range(3):
    print("Connection could not be established.")

#2
# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network
connection_attempts = 1
# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`
for i in range(connection_attempts):
    print("Connection could not be established")

#3
# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network
connection_attempts = 0
# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number
while connection_attempts <= 5:
    print("Connection could not be established.")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration) 
    connection_attempts = connection_attempts + 1
  
#4
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For loop that displays the elements of `ip_addresses` one at a time
for i in ip_addresses:
    print(i)

#5
# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
for i in ip_addresses:
	if i in allow_list:
		print(i+" IP address is allowed")
	else:
		print(i+" IP address is not allowed")

#6
# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]
# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
for i in ip_addresses:
	if i in allow_list:
		print(i+"IP address is allowed")
	else:
		print(i+"IP address is not allowed. Further investigation of login activity required")
		break

#7
# Assign the loop variable `i` to an initial value of 5000
i = 5000
# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
while i <= 5150:
    print (i)
    i = i + 5

#8
# Assign the loop variable `i` to an initial value of 5000
i = 5000
# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100
while i <= 5150: 
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5
