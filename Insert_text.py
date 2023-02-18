import os

insert_text = input("Enter the text to insert: ")
insert_pos = int(input("Enter the comma position to insert the text after (0 to insert at beginning): "))

cwd = os.getcwd()

for filename in os.listdir(cwd):
    if filename.endswith(".txt"):
        updated_lines = []
        with open(filename, "r") as f:
            for line in f:
                line_list = line.strip().split(",")
                if insert_pos == 0:
                    line_list.insert(0, insert_text)
                else:
                    line_list.insert(insert_pos, insert_text)
                updated_lines.append(",".join(line_list))
        with open(filename, "w") as f:
            for line in updated_lines:
                f.write(line + "\n")
