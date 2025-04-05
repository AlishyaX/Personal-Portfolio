# Project Details

#This function displays the details of each projects with the information given from the list of dictionaries 'projects'
def show_project_details(project):
    print("\nProject Name:", project['name'])
    print("Description:", project['description'])
    print("Process:", project['process'])
    print("Lessons Learned:", project['lessons'])
    print("Role:", project['role'])
    print("\n")
