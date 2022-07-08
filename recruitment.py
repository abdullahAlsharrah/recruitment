def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python","C++","React Native"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for count,skill in enumerate(skills, start=1):
        print(count,skill)
    
    
    ...


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    skill_1=input("Choose a skill from above by entering its number: ")
    skill_2=input("Choose a skill from above by entering its number: ")
    user_skills = []
    for count,skill in enumerate(skills, start=1):
        if(count == int(skill_1) or count == int(skill_2)):
            user_skills.append(skill) 
    return user_skills
    ...


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {}
    name=input("What's your name? ")
    age=input("How old are you? ")
    experience=input("How many years of experience do you have? ")
    cv["name"]=name
    cv["age"]=int(age)
    cv["experience"]=int(experience)
    show_skills(skills)
    cv["skills"]= get_user_skills(skills)

    return cv
    ...


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if(desired_skill in cv["skills"] and cv["experience"]>= 3 and cv["age"]>=25 and cv["age"]<40 ):
        return True
    else:
        return False
        
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions: ")
    skills = get_skills()
    desired_skill = skills[2]
    cv = get_user_cv(skills)
    check =check_acceptance(cv,desired_skill)
    name =cv["name"]
    if(check == True):
        print(f"You have been accepted, {name}.")
    else:
         print(f"Sorry, You have been rejected, {name}.")
    ...


if __name__ == "__main__":
    main()
