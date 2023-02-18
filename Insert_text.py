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

# prompt the user to enter the insert text and comma position
insert_text = input("Enter the text to insert: ")
insert_pos = int(input("Enter the comma position to insert the text after (0 to insert at beginning): "))

# loop through all files in the specified directory
for filename in os.listdir(cwd):
    # check if the file is a txt file
    if filename.endswith(".txt"):
        # create a list to store the updated lines
        updated_lines = []
        # open the file for reading
        with open(os.path.join(cwd, filename), "r") as f:
            # loop through each line in the file
            for line in f:
                # split the line into a list of strings
                line_list = line.strip().split(",")
                # insert the text at the specified position
                if insert_pos == 0:
                    line_list.insert(0, insert_text)
                else:
                    line_list.insert(insert_pos, insert_text)
                # join the list back into a string and add it to the updated lines list
                updated_lines.append(",".join(line_list))
        # open the file for writing
        with open(os.path.join(cwd, filename), "w") as f:
            # write each updated line to the file
            for line in updated_lines:
                f.write(line + "\n")
