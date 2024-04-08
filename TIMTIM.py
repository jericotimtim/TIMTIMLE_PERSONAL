# TIMTIM, ABRAHAM JERICO C. 
#Technology Job Search Site Simulation for the Philippines
import random

# Technology job listings with additional details
technology_jobs_library = {
    "Software Development": [
        {
            "title": "Python Developer",
            "location": "Philippines, Manila",
            "salary_range": "PHP 800,000 - PHP 1,200,000 per year",
            "company": "Samsan Tech Innovations Inc.",
            "requirements": "Bachelor's degree in computer science or equivalent discipline, fluency in Python programming, and experience with the Django framework",
            "description": "Samsan Tech Innovations Inc. is looking for a competent Python Developer to join our dynamic team. The ideal applicant should have extensive Python development experience and be able to work on difficult projects autonomously."
        },
        {
            "title": "Web Developer",
            "location": "Philippines, Batangas City",
            "salary_range": "PHP 600,000 - PHP 900,000 per year",
            "company": "Infinum PH",
            "requirements": "Bachelor's degree in computer science or similar discipline, fluency in HTML, CSS, JavaScript, and experience with the React framework.",
            "description": "Infinum PH is looking for a competent Web Developer to help with our unique web projects. The ideal candidate will be passionate about web development and capable of working well with our team."
        },
        {
            "title": "Mobile App Developer",
            "location": "Philippines, Davao City",
            "salary_range": "PHP 700,000 - PHP 1,000,000 per year",
            "company": "Mobizen Solutions",
            "requirements": "A bachelor's degree in computer science or a related subject, experience in mobile app development (iOS/Android), and knowledge of Swift/Kotlin programming languages",
            "description": "Mobizen Solutions is looking for an experienced Mobile App Developer to design and develop creative mobile applications. The ideal candidate would have a strong background in mobile app development and a desire to create user-friendly interfaces."
        }
    ],
    "Data Science": [
        {
            "title": "Data Analyst",
            "location": "Philippines, Makati City",
            "salary_range": "PHP 900,000 - PHP 1,300,000 per year",
            "company": "Capgemini Insights Co.",
            "requirements": "A bachelor's degree in statistics, mathematics, computer science, or similar subject, SQL fluency, and experience with data visualization tools (e.g., Tableau)",
            "description": "Capgemini Insights Co. is looking for a competent Data Analyst to analyze massive datasets and deliver relevant insights to clients. The ideal candidate would have excellent analytical skills and a thorough comprehension of statistical approaches."
        },
        {
            "title": "Machine Learning Engineer",
            "location": "Philippines, Quezon City",
            "salary_range": "PHP 1,000,000 - PHP 1,500,000 per year",
            "company": "Magnetar Inc.",
            "requirements": "A master's or doctoral degree in computer science, mathematics, or a related discipline, and competence with machine learning techniques and frameworks (e.g., TensorFlow, PyTorch)",
            "description": "Magnetar Inc. is looking for a competent Machine Learning Engineer to create cutting-edge machine learning models and algorithms. The ideal candidate will have a good background in mathematics and a love for artificial intelligence."
        },
        {
            "title": "Big Data Engineer",
            "location": "Philippines, Taguig City",
            "salary_range": "PHP 1,200,000 - PHP 1,800,000 per year",
            "company": "Cognizant Solutions PH",
            "requirements": "A bachelor's or master's degree in computer science, engineering, or a similar subject, familiarity with big data technologies (e.g., Hadoop, Spark), and skill in programming languages like Java or Scala",
            "description": "Cognizant Solutions PH is searching for an experienced Big Data Engineer to help design and build large-scale data processing solutions. The ideal applicant will have extensive technical knowledge and expertise working with distributed computing frameworks."
        }
    ],
    "IT Support": [
        {
            "title": "System Administrator",
            "location": "Philippines, Pasig City",
            "salary_range": "PHP 600,000 - PHP 900,000 per year",
            "company": "DXC Technologies PH",
            "requirements": "A bachelor's degree in information technology or a similar discipline, and familiarity with system administration activities (e.g., network configuration, server maintenance)",
            "description": "DXC Technologies PH is looking for a System Administrator to oversee our network infrastructure and ensure the seamless running of our systems. The ideal candidate will be adept at troubleshooting and possess a thorough understanding of IT principles."
        },
        {
            "title": "Network Engineer",
            "location": "Philippines, Makati City",
            "salary_range": "PHP 700,000 - PHP 1,000,000 per year",
            "company": "Globe Telecom Inc.",
            "requirements": "Bachelor's degree in Computer Science, Information Technology, or similar subject, CCNA/CCNP certification, and experience in network design and implementation",
            "description": "Globe Telecom Inc. is looking for a Network Engineer to design, develop, and manage our network infrastructure. The ideal applicant will have extensive experience with network technology and a proactive approach to problem solutions."
        },
        {
            "title": "Help Desk Technician",
            "location": "Philippines, Quezon City",
            "salary_range": "PHP 500,000 - PHP 800,000 per year",
            "company": "TEKsystems Inc.",
            "requirements": "Associate degree in information technology or equivalent profession, experience in providing technical support to end users, and knowledge with help desk software.",
            "description": "TEKsystems Inc. is seeking a Help Desk Technician to provide technical support to our clients. The ideal applicant would have strong communication skills and a customer-centric mindset."
        }
    ]
}

# Additional employer accounts and listings
employer_accounts = {
    "employer1": {"password": "password1"},
    "employer2": {"password": "password2"},
    "employer3": {"password": "password3"}
}

employer_jobs_library = {
    "employer1": {
        "Web Developer": {"location": "Philippines, Batangas", "salary_range": "PHP 700,000 - PHP 1,000,000 per year"},
        "Data Scientist": {"location": "Philippines, Quezon City", "salary_range": "PHP 900,000 - PHP 1,200,000 per year"}
    },
    "employer2": {
        "IT Support Specialist": {"location": "Philippines, Makati City", "salary_range": "PHP 600,000 - PHP 900,000 per year"},
        "Network Administrator": {"location": "Philippines, Pasig City", "salary_range": "PHP 800,000 - PHP 1,100,000 per year"}
    },
    "employer3": {
        "Software Engineer": {"location": "Philippines, Cebu City", "salary_range": "PHP 750,000 - PHP 1,100,000 per year"},
        "Database Administrator": {"location": "Philippines, Taguig City", "salary_range": "PHP 800,000 - PHP 1,200,000 per year"}
    }
}

# User accounts and preferences
user_accounts = {}

# Function for main user interaction
def main_user():
    print("\n____________________________________________")
    print("Welcome! Find Tech Jobs in the Philippines")
    print("[1] Registration")
    print("[2] Sign-in")
    print("[3] Employer")
    print("[4] Exit")
    print("_____________________________________________")
    
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                register()
            elif choice == 2:
                sign_in()
            elif choice == 3:
                main_employer()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid input. Kindly try again!")
        except ValueError:
            print("The input is invalid. Please select a valid option (1, 2, 3, or 4).")

# Function for user registration
def register():
    username = input("Create your username: ")
    while True:
        if not username:
            print("The username cannot be empty!")
            username = input("Create your username: ")
            continue
        if username in user_accounts:
            print("The username already exists. Please try another name!")
            username = input("Create your username: ")
            continue
        break
    
    while True:
        password = input("Create a password (at least 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters!")
        else:
            user_accounts[username] = {'password': password}
            print("Sign-up Successful")
            main_user()
            break

# Function for user sign-in
def sign_in():
    print("Sign-in!")
    while True:
        username = input("Please enter your username: ") 
        if not username:
            print("The username cannot be empty!")
            continue
        password = input("Please enter your password: ")
        if user_accounts.get(username) and user_accounts[username]['password'] == password:
            print("Sign-in Successful")
            user_menu(username)
        else:
            print("Invalid username or password")
            break

# Function to display user menu after sign-in
def user_menu(username, profile=None):    
    print("\n________________________")
    print("Hello, User!")
    print("[1] Find Job")
    print("[2] Configure Profile")
    print("[3] Visit Profile")
    print("[4] Profession Guidance")
    print("[5] Virtual Interview")
    print("[6] Curriculum Vitae Generator")
    print("[7] Exit")
    print("________________________")
    
    while True:
        try:
            choice = int(input("Please Enter your choice: "))
            if choice == 1:
                job_search()
            elif choice == 2:
                profile = edit_profile(profile)
            elif choice == 3:
                check_profile(profile)
            elif choice == 4:
                career_advice()
            elif choice == 5:
                simulated_interview()
            elif choice == 6:
                resume_builder()
            elif choice == 7:
                main_user()
            else:
                print("Invalid Input. Please choose again!")
            user_menu(username, profile)
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-7).")

# Function for job search functionality
def job_search():
    print("\n__________________________________")
    print("Let's Begin Your Job Search!")
    print("[1] Job Category")
    print("[2] In Demand Jobs")
    print("[3] Wage Range Options")
    print("[4] Go back")
    print("__________________________________")

    while True:
        try:
            choice = int(input("Please Enter your Choice: "))
            if choice == 1:
                job_classification()
            elif choice == 2:
                job_trend()
            elif choice == 3:
                salary_range()
            elif choice == 4:
                user_menu(username)
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-4).")

# Function to display job classifications
def job_classification():
    print("\n__________________________________")
    print("Let's Begin Your Job Search!")
    print("Job Category:")
    job_categories = list(technology_jobs_library.keys())
    for i, category in enumerate(job_categories, 1):
        print(f"[{i}] {category}")
    print(f"[{len(job_categories) + 1}] Go back")
    print("__________________________________")
    choice = int(input("Please Enter your Choice: "))
    
    if 1 <= choice <= len(job_categories):
        selected_category = job_categories[choice - 1]
        print(f"\n{selected_category} Jobs")
           
        for job in technology_jobs_library[selected_category]:
            print(f"{job['title']}:")
            print(f"   Location: {job['location']}")
            print(f"   Salary Range: {job['salary_range']}")
            print(f"   Company: {job['company']}")  
            print("\n")
    elif choice == len(job_categories) + 1:
        job_search()
    else:
        print("Invalid input. Please enter a valid choice.")

# Function to display popular job listings
def job_trend():
    popular_jobs = random.sample(technology_jobs_library[random.choice(list(technology_jobs_library.keys()))], 3)
    
    print("\n__________________________________")
    print("In Demand Jobs")
    print("__________________________________")
    for job in popular_jobs:
        print(f"Title: {job['title']}")
        print(f"Location: {job['location']}")
        print(f"Salary Range: {job['salary_range']}")
        print(f"Company: {job['company']}")
        print("\n")
    
    print("[0] Go back to Job Menu")
    while True:
        go_back = input("Press 0 to go back: ")
        if go_back == '0':
            job_search()
        else:
            print("Invalid Input!")
            continue

# Function for salary range selection
def salary_range():
    print("\n__________________________________")
    print("Wage Range Options")
    print("__________________________________")
    min_salary = int(input("Enter minimum salary range: "))
    max_salary = int(input("Enter maximum salary range: "))
    
    print("\nJobs within the specified salary range:")
    for category in technology_jobs_library:
        for job in technology_jobs_library[category]:
            salary = int(job['salary_range'].split(' ')[1].replace(',', ''))
            if min_salary <= salary <= max_salary:
                print(f"{job['title']}:")
                print(f"   Location: {job['location']}")
                print(f"   Salary Range: {job['salary_range']}")
                print(f"   Company: {job['company']}")  
                print("\n")

# Function to edit user profile
def edit_profile(profile):
    if not profile:
        profile = {}
    
    print("\n__________________________________")
    print("Configure Profile")
    print("__________________________________")
    
    while True:
        name = input("Enter your name: ")
        if not name:
            print("Name cannot be empty!")
            continue
        else:
            profile['Name'] = name
            break
            
    while True:
        age = input("Enter your age: ")
        if not age:
            print("Age cannot be empty!")
            continue
        else:
            profile['Age'] = age
            break
            
    while True:
        location = input("Enter your location: ")
        if not location:
            print("Location cannot be empty!")
            continue
        else:
            profile['Location'] = location
            break
    
    print("Profile Updated Successfully!")
    return profile

# Function to check user profile
def check_profile(profile):
    if not profile:
        print("Profile is empty. Please edit your profile!")
    else:
        print("\n__________________________________")
        print("User Profile")
        print("__________________________________")
        for key, value in profile.items():
            print(f"{key}: {value}")
        print("\n")

# Function for career advice
def career_advice():
    print("\n__________________________________")
    print("Profession Guidance")
    print("__________________________________")
    print("1. How to Prepare for a Tech Interview?")
    print("2. Career Growth in Technology Sector")
    print("3. Importance of Networking in Tech Industry")
    print("4. Go back")
    print("__________________________________")
    
    while True:
        try:
            choice = int(input("Please Enter your Choice: "))
            if choice == 1:
                print("Here are some tips to prepare for a tech interview:")
                print("- Practice coding problems on platforms like LeetCode and HackerRank.")
                print("- Review fundamental concepts such as data structures and algorithms.")
                print("- Research the company and be prepared to discuss your past projects.")
                print("- Practice solving problems aloud to improve communication skills.")
            elif choice == 2:
                print("The technology sector offers vast opportunities for career growth.")
                print("You can specialize in areas such as software development, data science, cybersecurity, and more.")
                print("Continuous learning and staying updated with industry trends are key to advancing your career.")
            elif choice == 3:
                print("Networking is crucial in the tech industry for career advancement and opportunities.")
                print("Attend industry events, join tech communities, and connect with professionals on platforms like LinkedIn.")
                print("Building a strong network can provide valuable insights, mentorship, and job referrals.")
            elif choice == 4:
                user_menu(username)
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-4).")

# Function for simulated interview
def simulated_interview():
    print("\n__________________________________")
    print("Virtual Interview")
    print("__________________________________")
    print("Let's simulate a technical interview scenario.")
    print("You will be asked a series of technical questions.")
    print("Prepare your responses and demonstrate your problem-solving skills.")
    print("__________________________________")

    technical_questions = [
        "What is the difference between list and tuple in Python?",
        "Explain the concept of object-oriented programming.",
        "How does a binary search algorithm work?",
        "What is the purpose of a virtual function in C++?",
        "What are the benefits of using version control systems like Git?",
        "Describe the process of deploying a web application to a server."
    ]

    for i, question in enumerate(technical_questions, 1):
        input(f"\nQuestion {i}: {question}\nPress Enter to continue...")

    print("\nThank you for participating in the simulated interview!")
    user_menu(username)

# Function for resume building
def resume_builder():
    print("\n__________________________________")
    print("Curriculum Vitae Generator")
    print("__________________________________")
    print("Let's create your resume.")
    print("Provide information about your education, skills, experience, etc.")
    print("__________________________________")

    resume = {}

    while True:
        education = input("Enter your educational background: ")
        if not education:
            print("Education field cannot be empty!")
            continue
        else:
            resume['Education'] = education
            break

    while True:
        experience = input("Enter your work experience: ")
        if not experience:
            print("Experience field cannot be empty!")
            continue
        else:
            resume['Experience'] = experience
            break

    while True:
        skills = input("Enter your skills (comma-separated): ")
        if not skills:
            print("Skills field cannot be empty!")
            continue
        else:
            resume['Skills'] = skills.split(',')
            break

    print("\nYour Resume:")
    for key, value in resume.items():
        if isinstance(value, list):
            value = ', '.join(value)
        print(f"{key}: {value}")

    user_menu(username)

# Function for employer interaction
def main_employer():
    print("\n____________________________________________")
    print("Employer Portal - Technology Job Listings")
    print("[1] Sign-in")
    print("[2] Register")
    print("[3] Exit")
    print("____________________________________________")
    
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                employer_sign_in()
            elif choice == 2:
                employer_register()
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid Input. Please try again!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1, 2, or 3).")

# Function for employer sign-in
def employer_sign_in():
    print("Employer Sign-in!")
    while True:
        username = input("Please enter your username: ") 
        if not username:
            print("Username cannot be empty!")
            continue
        password = input("Please enter your password: ")
        if employer_accounts.get(username) and employer_accounts[username]['password'] == password:
            print("Sign-in Successful")
            employer_menu(username)
        else:
            print("Invalid username or password")
            break

# Function for employer registration
def employer_register():
    username = input("Create your username: ")
    while True:
        if not username:
            print("Username cannot be empty!")
            username = input("Create your username: ")
            continue
        if username in employer_accounts:
            print("Username already exists. Please try another name!")
            username = input("Create your username: ")
            continue
        break
    
    while True:
        password = input("Create your password (Must be at least 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters!")
        else:
            employer_accounts[username] = {'password': password}
            print("Sign-up Successful")
            main_employer()
            break

# Function for employer menu
def employer_menu(username):
    print("\n________________________")
    print("Greetings Employer!")
    print("[1] Post Job Listing")
    print("[2] View Job Applicants")
    print("[3] Exit")
    print("________________________")
    
    while True:
        try:
            choice = int(input("Please Enter your choice: "))
            if choice == 1:
                post_job_listing(username)
            elif choice == 2:
                view_job_applicants()
            elif choice == 3:
                main_employer()
            else:
                print("Invalid Input. Please choose again!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-3).")

# Function to post job listings
def post_job_listing(username):
    print("\n__________________________________")
    print("Post Job Listing")
    print("__________________________________")
    print("Enter job details:")
    job_title = input("Job Title: ")
    location = input("Location: ")
    salary_range = input("Salary Range: ")
    
    if username in employer_jobs_library:
        employer_jobs_library[username][job_title] = {"location": location, "salary_range": salary_range}
    else:
        employer_jobs_library[username] = {job_title: {"location": location, "salary_range": salary_range}}
    
    print("Job listing posted successfully!")
    employer_menu(username)

# Function to view job applicants
def view_job_applicants():
    print("\n__________________________________")
    print("View Job Applicants")
    print("__________________________________")
    print("Enter job title to view applicants:")
    for employer, jobs in employer_jobs_library.items():
        print(f"{employer}:")
        for job_title, details in jobs.items():
            print(f"    {job_title}")
    selected_employer = input("Enter employer username: ")
    selected_job = input("Enter job title: ")
    
    print("\nList of applicants for the job:")
    for user, profile in user_accounts.items():
        if user in job_applicants and selected_employer in job_applicants[user] and selected_job in job_applicants[user][selected_employer]:
            print(f"Applicant: {profile['Name']}")
            print(f"Location: {profile['Location']}")
            print("\n")

# Starting point of the program
if __name__ == "__main__":
    main_user()
