def get_student_level():

    print("\nSelect Student Level:\n")

    print("1. Class 6")
    print("2. Class 7")
    print("3. Class 8")
    print("4. Class 9")
    print("5. Class 10")

    choice = input("\nEnter Choice: ")

    mapping = {
        "1": "Class 6",
        "2": "Class 7",
        "3": "Class 8",
        "4": "Class 9",
        "5": "Class 10"
    }

    return mapping.get(choice, "Class 8")


def get_language():

    print("\nSelect Language:\n")

    print("1. English")
    print("2. Hindi")
    print("3. Auto Detect")

    choice = input("\nEnter Choice: ")

    mapping = {
        "1": "English",
        "2": "Hindi",
        "3": "Auto"
    }

    return mapping.get(choice, "English")