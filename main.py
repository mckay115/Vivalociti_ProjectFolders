import os
import platform

# Variables for the System
home_dir = os.path.expanduser("~")
lg_sp_dir = f'{home_dir}\Lamacchia Group\Vivalociti - Storage'

# File creation functions

def create_project(client_name, project_name, project_number, project_city, project_state):
    project_dir = f'{lg_sp_dir}\Client Specific Files\{client_name}\{project_city}, {project_state} -- {project_number}'
    try:
        os.makedirs(project_dir)
    except:
        print('Creation failed')
        quit()







'''
All Main Functions will happen below this line
'''

# Check that the OS is Windows, if not: End the Process
if platform.system() == 'Windows':
    print('System OS is a Match')
else:
    print('Program not optimized for non-Windows platforms.')
    print('Exiting System')
    quit()

# Check that the SharePoint directory exists
if os.path.isdir(lg_sp_dir):
    print('SharePoint Directory Found')
else:
    print('SharePoint mounting location not found. Please try setting up SharePoint again.')


name = input('What is the name of the client?: ')
number = input('What is the project number?: ')
city = input('What city is the project located in?: ')
state = input('What state is the project in?: ')

create_project(name, 'NA', number, city, state)