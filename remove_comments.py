import os

directory_path = input("Enter directory path: ")

# Create a new sub-directory named "new"
new_directory_path = os.path.join(directory_path, "new")
if not os.path.exists(new_directory_path):
    os.makedirs(new_directory_path)

for file_name in os.listdir(directory_path):
    if file_name.endswith(".ini"):
        file_path = os.path.join(directory_path, file_name)
        new_file_path = os.path.join(new_directory_path, file_name)
        with open(file_path, "r") as f, open(new_file_path, "w") as new_file:
            for line in f:
                # Remove any text after a semicolon
                line = line.split(";")[0]
                # Remove any leading or trailing whitespace
                line = line.strip()
                # If the line is empty or starts with a square bracket, write it as is
                if not line or line[0] == "[":
                    new_file.write(line + "\n")
                # Otherwise, replace all consecutive whitespace characters with a single space
                else:
                    line = " ".join(line.split())
                    new_file.write(line + "\n")

