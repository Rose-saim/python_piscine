def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: " + str(object) + " " + str(type(object)))
    elif isinstance(object, float):
        print("Cheese: " + str(object) + " " + str(type(object)))
    elif isinstance(object, bool):
        print("Fake: " + str(object) + " " + str(type(object)))
    elif isinstance(object, int):
        print("Zero: " + str(object) + " " + str(type(object)))
    elif isinstance(object, str) and len(object) == 0:
        print("Empty: " + str(object) + " " + str(type(object)))
    else:
        print("Type not found")
        return 1
    return 0
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))