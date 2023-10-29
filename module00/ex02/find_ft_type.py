def all_thing_is_obj(object: any) -> int:
    object_type = type(object).__name__
    object_type = object_type.capitalize()
    if type(object) is int:
        print ("Type not found")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{object_type} : {type(object)}")
    return 42
