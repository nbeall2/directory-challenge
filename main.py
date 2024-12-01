directory = {}

# Add each folder to the directory as needed
def add_to_directory(input):
    path = input.split('/')
    current_index = directory
    
    for folder in path:
        if folder not in current_index:
            current_index[folder] = {}
        current_index = current_index[folder]
    return

# Check if folder exists, if it does, then add it to the new location and delete the old instance. Otherwise return error
def move_to_directory(input):
    # Split the input into source and destination
    source, destination = input.split(' ')
    source_path = source.split('/')
    destination_path = destination.split('/')
    
    # Navigate to the source directory
    current = directory
    for folder in source_path[:-1]:
        if folder not in current:
            print(f'Cannot move {source} - path does not exist')
            return
        current = current[folder]
    
    # Check if the source directory to move exists
    if source_path[-1] not in current:
        print(f'Cannot move {source} - directory does not exist')
        return
    
    # Store the directory to move
    directory_to_move = current[source_path[-1]]
    
    # Navigate to the destination directory
    current_dest = directory
    for folder in destination_path:
        if folder not in current_dest:
            current_dest[folder] = {}
        current_dest = current_dest[folder]
    
    # Add the directory to the new location
    current_dest[source_path[-1]] = directory_to_move
    
    # Delete the old instance
    del current[source_path[-1]]
    print(f'Directory {source} moved to {destination} successfully')
    return

# Working: Recursive Function: Read and print each nested key in the directory dict
def list_from_directory(directory, sep=''):
    for key in sorted(directory.keys()):
        print(sep + key)
        if directory[key]:
            # add a tab every time we index further
            list_from_directory(directory[key], sep + '\t')

# Working: Find the nested key using input params, attempt to remove key if it exists
def delete_from_directory(input):
    path = input.split('/')
    current = directory
    
    # Navigate to the parent directory
    for folder in path[:-1]:
        if folder not in current:
            print(f'Cannot delete {input} - path does not exist')
            return
        current = current[folder]
    
    # Check if the directory to delete exists
    if path[-1] not in current:
        print(f'Cannot delete {input} - directory does not exist')
        return
    
    # Delete the directory
    del current[path[-1]]
    print(f'Directory {input} deleted successfully')
    return

# Working: Switchboard based on actions and inputs (if needed), certain actions require inputs
def process_user_inputs(action, input=None):
    match action:
        case 'CREATE':
            if (input):
                add_to_directory(input)
            else:
                print('There is no input')
        case 'MOVE':
            if (input):
                move_to_directory(input)
            else:
                print('MOVE requires a folder and a destination')
            return
        case 'LIST':
            list_from_directory(directory)
            return
        case 'DELETE':
            if (input):
                delete_from_directory(input)
            else:
                print('There is no input')
        case _:
            return 'Sorry, that action does not exist'

# Working: intialize instance and process user input
def main():
    while True:
        try:
            user_input = input("")
                
            # Split into command and input (if provided)
            parts = user_input.split(' ', 1)
            
            # On the off-chance someone forgets to capitalize input
            command = parts[0].upper()
            
            # Check if input is provided
            if len(parts) > 1:
                inputs = parts[1]
            else:
                inputs = None
                
            process_user_inputs(command, inputs)
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()