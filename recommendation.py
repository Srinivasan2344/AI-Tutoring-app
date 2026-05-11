courses = {

    "python": [
        "Python Basics",
        "Advanced Python"
    ],

    "ai": [
        "Introduction to AI",
        "Machine Learning"
    ],

    "web": [
        "HTML",
        "CSS",
        "JavaScript"
    ]
}



interest = input(
    "Enter your interest: "
).lower()


if interest in courses:

    print(
        "\nRecommended Courses:\n"
    )

    for course in courses[interest]:

        print(course)

else:

    print(
        "No courses found"
    )