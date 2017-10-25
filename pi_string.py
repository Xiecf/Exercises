filename = r'C:\Documents and Settings\Administrator\桌面\Python_work\text_files\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' 
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
print(pi_string[:12])
