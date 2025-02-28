from django.shortcuts import render
from .solver import TimetableSolver
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')


def generate(request):
    if request.method == 'POST':
        sections = request.POST.getlist('section_name')
        
        courses = {}
        course_names = request.POST.getlist('course_name')
        course_sections = request.POST.getlist('course_section')
        for name, section in zip(course_names, course_sections):
            if section not in courses:
                courses[section] = []
            courses[section].append(name)
        
        professors = {}
        professor_courses = request.POST.getlist('professor_course')
        professor_names = request.POST.getlist('professor_name')
        for course, name in zip(professor_courses, professor_names):
            professors[course] = name
        
        course_time_requirements = {}
        time_courses = request.POST.getlist('time_course')
        time_requirements = request.POST.getlist('time_requirement')
        for course, requirement in zip(time_courses, time_requirements):
            course_time_requirements[course] = int(requirement)
        
        days = request.POST.getlist('day_name')
        time_slots = request.POST.getlist('time_slot')

        solver = TimetableSolver(sections, courses, professors, course_time_requirements, days, time_slots)
        solver.define_objective()
        solver.add_constraints()
        solver.solve()
        timetable = solver.get_weekly_timetable()

        return render(request, 'generate.html', {'timetable': timetable, 'time_slots': time_slots})

    return render(request, 'generate.html')


# {"A": ["Maths", "Physics", "Chemistry", "FSD"],"B": ["Maths", "DMW", "Chemistry", "Sanskrit"],"C": ["Sports", "Physics", "Biology", "Hindi"],"D": ["Maths", "DL", "Chemistry", "Sanskrit"]}
# {"Maths": "Prof A","Physics": "Prof B","Chemistry": "Prof C","FSD": "Prof D","DMW": "Prof E","Sports": "Prof A","DL": "Prof B","Biology": "Prof C","Sanskrit": "Prof D","Hindi": "Prof E"}
# {"Maths": 5,"Physics": 5,"Chemistry": 5,"FSD": 5,"DMW": 5,"Sports": 3,"DL": 5,"Biology": 5,"Sanskrit": 5,"Hindi": 7}