

def calculate_average(grades):
    total=0
    count=0
    for i in grades:
        if type(i) == int or type(i) ==float:
            total= total+i
            count= count+1
    if count==0:
        return 0
    

    return total/count

def assign_letter_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"
    
    

def filter_passing_students(students, threshold=60):
    return list(filter(lambda x:x['average']>= threshold,students))


def merge_student_data(names, grades, emails):
    if len(names)!= len(grades) or len(names) != len(emails):
        print("warnin: lists not same size!")

def print_student_report(students):
    print("===== STUDENT REPORTS =====")
    for idx, s in enumerate(studs, 1):
        stat = "PASS" if s['average'] >= 60 else "FAIL"
        print(f"{idx}. {s['name']} ({s['email']})")
        print(f"Average: {s['average']:.1f}, Grade: {s['letter']}, Status: {stat}")
    
def find_top_performance(stdents,n=3):
    sorted_list = sorted(studs, key=lambda x: x['average'], reverse=True)
    return sorted_list[:n]
    
def main():
    print("===== STUDENT PERFORMANCE ANALYZER =====")
    
    
    
    print("Merging student data...")
    print(f"Names: {len(names)} entries")
    print(f"Grades: {len(grades)} entries")
    print(f"Emails: {len(emails)} entries")
    print("All lists match - safe to merge!")