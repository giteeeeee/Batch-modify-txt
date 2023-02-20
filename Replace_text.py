import os

# prompt the user to enter a directory location for modifying text files
while True:
    dir_path = input("Enter the directory path for modifying txt files (leave empty to use the same directory as the script): ").strip()
    if not dir_path:
        cwd = os.getcwd()
        break
    if os.path.isdir(dir_path):
        cwd = dir_path
        break
    else:
        print("Directory not found. Please enter a valid directory path.")

# Ask the user to input text to replace in the .txt files
old_text = input("Enter the text to replace: ")
new_text = input("Enter the replacement text (leave empty to delete the text entered above): ")

# Iterate over each file in the directory
for filename in os.listdir(cwd):
    if filename.endswith(".txt"):
        # Read the contents of the file
        with open(os.path.join(cwd, filename), "r") as file:
            contents = file.read()
        
        # Replace the text in the file
        new_contents = contents.replace(old_text, new_text)

        # Write the updated contents back to the file
        with open(os.path.join(cwd, filename), "w") as file:
            file.write(new_contents)
