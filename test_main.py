from main import process_user_inputs, directory

def test_directory_commands():
    global directory
    directory.clear()
    
    # Test CREATE commands
    process_user_inputs('CREATE', 'fruits')
    process_user_inputs('CREATE', 'vegetables')
    process_user_inputs('CREATE', 'grains')
    process_user_inputs('CREATE', 'fruits/apples')
    process_user_inputs('CREATE', 'fruits/apples/fuji')
    
    # Check current directory
    assert directory == {'fruits': {'apples': {'fuji': {}}}, 'grains': {}, 'vegetables': {}}
    
    # Test additional CREATE and MOVE commands
    process_user_inputs('CREATE', 'grains/squash')
    process_user_inputs('MOVE', 'grains/squash vegetables')
    process_user_inputs('CREATE', 'foods')
    process_user_inputs('MOVE', 'grains foods')
    process_user_inputs('MOVE', 'fruits foods')
    process_user_inputs('MOVE', 'vegetables foods')
    
    # Test LIST command after moves
    assert directory == {'foods': {'fruits': {'apples': {'fuji': {}}},'grains': {},'vegetables': {'squash': {}}}}
    
    # Test DELETE commands
    assert process_user_inputs('DELETE', 'fruits/apples') is None  # Should print an error
    assert process_user_inputs('DELETE', 'foods/fruits/apples') is None  # Should delete successfully
    
    # Final LIST command
    assert directory == {'foods': {'fruits': {},'grains': {},'vegetables': {'squash': {}}}}

