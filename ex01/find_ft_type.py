def all_thing_is_obj(obj: any) -> int:
    types_dic = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: " is in the kitchen"
    }
    obj_type = type(obj)
    if obj_type in types_dic:
        if obj_type != str:
            print(types_dic[obj_type], ":", obj_type)
        else:
            print(obj + types_dic[obj_type], ":" , obj_type)
    else:
        print("Type not found")
    return 42
