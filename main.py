# main.py
from src.oop_homework.students import Student
from src.oop_homework.mentors import Lecturer, Reviewer
from src.oop_homework.utils import avg_students_grade, avg_lecturers_grade


def main():
    print("===== Полевые испытания =====")

    # 1. Создание экземпляров (по 2 каждого класса)
    student1 = Student("Алёхина", "Ольга", "Ж")
    student2 = Student("Иванов", "Егор", "М")
    lecturer1 = Lecturer("Иван", "Иванов")
    lecturer2 = Lecturer("Петр", "Петровский")
    reviewer1 = Reviewer("Пётр", "Петров")
    reviewer2 = Reviewer("Сергей", "Сергеев")

    # 2. Настройка курсов
    student1.courses_in_progress = ["Python", "Java"]
    student1.finished_courses = ["C++"]
    student2.courses_in_progress = ["Python", "Java"]
    student2.finished_courses = ["C++", "Git"]

    lecturer1.courses_attached = ["Python", "Java"]
    lecturer2.courses_attached = ["Python", "C++"]

    reviewer1.courses_attached = ["Python", "Java"]
    reviewer2.courses_attached = ["Python", "C++"]

    # 3. Проверяющие выставляют оценки студентам
    print("\n--- Выставление оценок студентам (Reviewer) ---")
    reviewer1.rate_hw(student1, "Python", 7)
    reviewer1.rate_hw(student1, "Python", 8)
    reviewer1.rate_hw(student1, "Java", 6)
    reviewer2.rate_hw(student2, "Python", 9)
    reviewer2.rate_hw(student2, "Python", 10)
    reviewer2.rate_hw(student2, "C++", 5)  # C++ у student2 в завершённых? В условии задания оценка ставится за курс в процессе изучения, но у нас для проверки можно разрешить
    # Однако по логике rate_hw проверяет, что курс в courses_in_progress, поэтому добавим его
    student2.courses_in_progress.append("C++")
    reviewer2.rate_hw(student2, "C++", 5)   # теперь ок

    print("Оценки student1:", student1.grades)
    print("Оценки student2:", student2.grades)

    # 4. Студенты выставляют оценки лекторам
    print("\n--- Выставление оценок лекторам (Student) ---")
    student1.rate_lecture(lecturer1, "Python", 9)
    student1.rate_lecture(lecturer1, "Python", 8)
    student1.rate_lecture(lecturer1, "Java", 7)
    student2.rate_lecture(lecturer2, "Python", 10)
    student2.rate_lecture(lecturer2, "Python", 9)
    student2.rate_lecture(lecturer2, "C++", 6)

    # Попробуем ошибочные сценарии (они не должны добавлять оценки)
    print("\n--- Проверка ошибок ---")
    result = student1.rate_lecture(lecturer1, "C++", 8)  # C++ нет у student1 в процессе
    print(f"Ошибка (курс не в процессе): {result}")
    result = student1.rate_lecture(lecturer2, "Python", 8)  # lecturer2 не прикреплён к Python? он прикреплён
    # Но lecturer2 привязан к Python, так что будет успешно
    # Давайте создадим ошибку: лектор не прикреплён к курсу
    lecturer3 = Lecturer("Ганс", "Клитке")
    lecturer3.courses_attached = ["JavaScript"]
    result = student1.rate_lecture(lecturer3, "Python", 8)
    print(f"Ошибка (лектор не ведёт курс): {result}")

    print("\nОценки lecturer1:", lecturer1.grades)
    print("Оценки lecturer2:", lecturer2.grades)

    # 5. Вывод информации через __str__
    print("\n--- Строковые представления ---")
    print("Reviewer1:")
    print(reviewer1)
    print("\nLecturer1:")
    print(lecturer1)
    print("\nStudent1:")
    print(student1)

    # 6. Сравнение лекторов и студентов
    print("\n--- Сравнение ---")
    print(f"Средняя оценка lecturer1: {lecturer1.average_grade():.2f}")
    print(f"Средняя оценка lecturer2: {lecturer2.average_grade():.2f}")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

    print(f"Средняя оценка student1: {student1.average_grade():.2f}")
    print(f"Средняя оценка student2: {student2.average_grade():.2f}")
    print(f"student1 < student2: {student1 < student2}")

    # 7. Утилитные функции (Задание №4)
    print("\n--- Утилитные функции ---")
    students_list = [student1, student2]
    avg_python = avg_students_grade(students_list, "Python")
    avg_java = avg_students_grade(students_list, "Java")
    print(f"Средняя оценка за ДЗ по Python среди всех студентов: {avg_python}")
    print(f"Средняя оценка за ДЗ по Java среди всех студентов: {avg_java}")

    lecturers_list = [lecturer1, lecturer2]
    avg_lect_python = avg_lecturers_grade(lecturers_list, "Python")
    avg_lect_cpp = avg_lecturers_grade(lecturers_list, "C++")
    print(f"Средняя оценка за лекции по Python среди всех лекторов: {avg_lect_python}")
    print(f"Средняя оценка за лекции по C++ среди всех лекторов: {avg_lect_cpp}")

    print("\n=== Полевые испытания завершены ===")


if __name__ == "__main__":
    main()