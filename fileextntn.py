
filename = input("Enter a file name (with extension): ")
if '.' in filename:
    extension = filename.split('.')
    print(f"The extension of the file is: {extension}")
else:
    print("No extension found.")
