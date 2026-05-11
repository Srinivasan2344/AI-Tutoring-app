students = [

    {
        "name": "Durai",
        "marks": 95
    },

    {
        "name": "Arun",
        "marks": 82
    },

    {
        "name": "Kumar",
        "marks": 45
    }
]



for student in students:

    print("\nStudent Name:",
    student["name"])

    print("Marks:",
    student["marks"])


    if student["marks"] >= 80:

        print("Performance: Excellent")

    elif student["marks"] >= 50:

        print("Performance: Average")

    else:

        print("Performance: Needs Improvement")