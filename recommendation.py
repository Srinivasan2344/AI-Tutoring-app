courses = {
    "Python Basics": "python coding beginner",
    "Machine Learning": "machine learning ai",
    "Data Science": "data analysis python",
    "Web Development": "html css javascript",
    "Artificial Intelligence": "deep learning neural networks"
}

user_interest = input("Enter your interest: ").lower()

found = False

for course, skills in courses.items():
    
    if user_interest in skills:
        print("\nRecommended Course:", course)
        found = True

if not found:
    print("\nNo matching course found")