import math
#start with personal information 
full_name = "Kabijah Hill"
student_email = "kabijahhill2000@gmail.com"
hometown = "Nashville, NC"
grad_semester = "Spring 2029"   # estimate, since  start at NC A&T Fall 2025
school_major = "Computer Science"

#academic data
current_courses = ["COMP 163", "MATH 131", "COMP 180", "HIST 106", "GEEN 111",]   # 
completed_courses = ["Intro to Engineering", "Pre-Calculus", "Pre-Trignometry", "Sociology"]  #all NCC courses
credit_hours = [3, 4, 3, 3]
gpa_history = [3.5, 3.6, 3.7, 3.5]   # going off my ncc transcript

#contact information
emergency_contact = ("Mom", "Ta-Tanisha Hill", "252-266-9058")
home_address = ("236 Regency Drive", "Nashville, NC", "27856")
instagram_stuff = ("Instagram", "@randomuser._.13", 389)
twitter_stuff = ("Twitter", "@donthaveone", 0)
birth_day = ("Birthday", "11", "29", "2005")

#interest tracking
current_skills = {"Python", "C++", "Creative Design", "Tutoring", "Technical Design"}
skills_tolearn = {"3D Animation", "Game Design Basics", "Digital Illustration", "3D Printing & Prototyping"}
career_intrests = {"Graphic Engineer", "CAD Drafter / Design Engineer", "Game Developer (Graphics)", "3D Animator",  "UX/UI Designer"} 
hobbies_set = {"Writing", "Gaming", "Reading", "Drawing", "Badminton"}
entertainment_backlog = {"Daria", "Dark Deception", "Rugrats", "Attack on Titan", "Tetris"}

#mapping stuff
course_credits = {"COMP 163": 3, "MATH 131": 4, "COMP 180": 3, "HIST 106": 3, "GEEN 111": 1}
course_prof = {"COMP 163": "Dr.Rhodes", "MATH 131": "Mr.Terkper", "COMP 180": "Ms.Nowaczyk-Pioro", "HIST 106": "Ms. Devoe", "GEEN 111": "Mr.Parrish"}
course_rooms = {"COMP 163": "MERIC 300", "MATH 131": "Crosby 106", "COMP 180": "MERIC 200", "HIST 106": "Online", "GEEN 111": "McNair 240"}
monthly_budget = {"Food": 25, "Entertainment": 10, "Books": 0, "Transportation": 15}
study_hours = {"Programming": 12, "Calculus": 10, "Discrete Sturcture": 4, "ENGI Collo": 1, "History": 3}
contact_directory = {"Mom": "252-266-9058", "Advisor": "336-285-4213", "Friend": "252-903-5207"}

#time for calculations
total_credits = sum(credit_hours)
cumlative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_study_hours = sum(study_hours.values())
academic_load = total_credits + total_study_hours
monthly_total = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget = monthly_total * 12
study_cost_per_hr = round(monthly_budget["Books"] / total_study_hours, 2)

#Analytics Calculations
total_followers = instagram_stuff[2] + twitter_stuff[2]
skills_difference = len(current_skills) - len(skills_tolearn)
contact_count = len(contact_directory)
backlog_count = len(entertainment_backlog)

academic_workload_score = total_credits * total_study_hours

#final output
print("=======================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=======================================================")

print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {grad_semester}")
print(f"Major: {school_major}")

print("\n=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumlative_gpa:.2f}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hr} per study hour\n")

print("Current Courses:")
for c in current_courses:
    print(f"{c} - {course_credits[c]} credits - {course_prof[c]} - {course_rooms[c]}")

print("\n=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_tolearn}")
print(f"Career Interests: {career_intrests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_tolearn)}")

print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_total}")
print(f"Food: ${monthly_budget['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget}")

print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_count} people in directory")

print("\n=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {backlog_count} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("================================================================")
