# src/oop_homework/utils.py

def avg_students_grade(students_list, course_name):
    """
    Вычисляет среднюю оценку за домашние задания по указанному курсу
    для всех переданных студентов.

    Args:
        students_list (list): Список объектов Student.
        course_name (str): Название курса.

    Returns:
        float: Средняя оценка (0.0, если оценок нет).
    """
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 2)


def avg_lecturers_grade(lecturers_list, course_name):
    """
    Вычисляет среднюю оценку за лекции по указанному курсу
    для всех переданных лекторов.

    Args:
        lecturers_list (list): Список объектов Lecturer.
        course_name (str): Название курса.

    Returns:
        float: Средняя оценка (0.0, если оценок нет).
    """
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 2)
