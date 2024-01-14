#1
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Display `import_file`
print(import_file)
# Display `remove_list`
print(remove_list)

#2
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# First line of `with` statement
with open(import_file, "w") as file:

#3
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Display `ip_addresses`
print(ip_addresses)

#4
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Display `ip_addresses`
print(ip_addresses)

#5
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`
for i in ip_addresses:
    # Display `element` in every iteration
    print(i)

#6
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
  # Build conditional statement
  # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)
# Display `ip_addresses` 
print(ip_addresses)

#7
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
  # Build conditional statement
  # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)
# Convert `ip_addresses` back to a string so that it can be written into the text file 
ip_addresses = " ".join(ip_addresses)    
# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
  # Rewrite the file, replacing its contents with `ip_addresses`
  file.write(ip_addresses)

#8
# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
  # Build conditional statement
  # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)
# Convert `ip_addresses` back to a string so that it can be written into the text file 
ip_addresses = " ".join(ip_addresses)       
# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
  # Rewrite the file, replacing its contents with `ip_addresses`
  file.write(ip_addresses)
# Build `with` statement to read in the updated file
with open(import_file, "r") as file:
    # Read in the updated file and store the contents in `text`
    text = file.read()
# Display the contents of `text`
print(text)

#9
# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this
def update_file(important_file, remove_list):
    # Build `with` statement to read in the initial contents of the file
    with open(import_file, "r") as file:
        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()
    # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()
    # Build iterative statement
    # Name loop variable `element`
    # Loop through `ip_addresses`
    for element in ip_addresses:
        # Build conditional statement
        # If current element is in `remove_list`,
        if element in remove_list:
            # then current element should be removed from `ip_addresses`
            ip_addresses.remove(element)
    # Convert `ip_addresses` back to a string so that it can be written into the text file 
    ip_addresses = " ".join(ip_addresses)       
    # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:
        # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)

  #10
  # Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this
def update_file(import_file, remove_list):
  # Build `with` statement to read in the initial contents of the file
  with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()
  # Use `.split()` to convert `ip_addresses` from a string to a list
  ip_addresses = ip_addresses.split()
  # Build iterative statement
  # Name loop variable `element`
  # Loop through `ip_addresses`
  for element in ip_addresses:  
    # Build conditional statement
    # If current element is in `remove_list`, 
    if element in remove_list:
      # then current element should be removed from `ip_addresses`
      ip_addresses.remove(element)
  # Convert `ip_addresses` back to a string so that it can be written into the text file 
  ip_addresses = " ".join(ip_addresses)       
  # Build `with` statement to rewrite the original file
  with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses`
    file.write(ip_addresses)
# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed
update_file(import_file, remove_list)
# Build `with` statement to read in the updated file
with open("allow_list.txt", "r") as file:
  # Read in the updated file and store the contents in `text`
  text = file.read()
# Display the contents of `text`
print(text)
