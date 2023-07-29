#Automatically create folder daily
import os
import datetime

def create_folder(day_number):
    folder_name = f"day{day_number:02}"
    os.makedirs(folder_name, exist_ok=True)

    # Create README.md
    readme_content = f"# Day {day_number} - \n## Concepts Practised\n\n##Assigment Title"
    with open(os.path.join(folder_name, "README.md"), "w") as readme_file:
        readme_file.write(readme_content)

    # Create main.py
    main_content = f"# Python code for Day {day_number}.\n"
    with open(os.path.join(folder_name, "main.py"), "w") as main_file:
        main_file.write(main_content)

    return folder_name, readme_content, main_content

def main():
    start_date = datetime.datetime(2023, 7, 26)
    today = datetime.datetime.now()
    day_number = (today - start_date).days + 1

    folder_name, readme_content, main_content = create_folder(day_number)

    print(f"Created folder: {folder_name}")
    print("\nREADME.md content:")
    print(readme_content)
    print("\nmain.py content:")
    print(main_content)

if __name__ == "main":
    main()