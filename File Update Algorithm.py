def update_file(import_file, remove_list):
  with open(import_file, "r") as file:
    ip_addresses = file.read()
  ip_addresses = ip_addresses.split()
  for element in ip_addresses:  
    if element in remove_list:
      ip_addresses.remove(element)
  ip_addresses = " ".join(ip_addresses)       
  with open(import_file, "w") as file:
    file.write(ip_addresses)
update_file(import_file, remove_list)
with open("allow_list.txt", "r") as file:
  text = file.read()
print(text)

#execute
update_file(allowed_list, remove_list)
