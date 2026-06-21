# tests/test_utils.py
import pytest
from src.oop_homework.utils import avg_students_grade, avg_lecturers_grade
from src.oop_homework.students import Student
from src.oop_homework.mentors import Lecturer


class TestAvgStudentsGrade:
    """Тесты для функции avg_students_grade."""

    @pytest.fixture
    def students(self):
        """Создаёт список студентов с оценками."""
        s1 = Student("A", "B", "М")
        s1.grades = {"Python": [5, 6], "Java": [7, 8]}
        s2 = Student("C", "D", "М")
        s2.grades = {"Python": [4, 5], "Java": [9, 10]}
        s3 = Student("E", "F", "М")
        s3.grades = {"C++": [1, 2]}  # не имеет курса Python
        return [s1, s2, s3]

    def test_avg_existing_course(self, students):
        """Средняя по курсу, который есть у нескольких студентов."""
        result = avg_students_grade(students, "Python")
        # Оценки: s1: 5,6; s2: 4,5 => всего [5,6,4,5] средняя = 20/4 = 5.0
        assert result == 5.0

    def test_avg_course_with_one_student(self, students):
        """Курс только у одного студента."""
        result = avg_students_grade(students, "Java")
        # Оценки: s1: 7,8; s2: 9,10 => всего 4 оценки, средняя = (7+8+9+10)/4 = 8.5
        assert result == 8.5

    def test_avg_course_no_students(self, students):
        """Курс отсутствует у всех студентов."""
        result = avg_students_grade(students, "Git")
        assert result == 0.0

    def test_avg_empty_list(self):
        """Пустой список студентов."""
        result = avg_students_grade([], "Python")
        assert result == 0.0

    def test_avg_student_with_no_grades(self):
        """Студент без оценок."""
        s = Student("X", "Y", "М")
        result = avg_students_grade([s], "Python")
        assert result == 0.0


class TestAvgLecturersGrade:
    """Тесты для функции avg_lecturers_grade."""

    @pytest.fixture
    def lecturers(self):
        """Создаёт список лекторов с оценками."""
        l1 = Lecturer("A", "B")
        l1.grades = {"Python": [8, 9], "Java": [6, 7]}
        l2 = Lecturer("C", "D")
        l2.grades = {"Python": [7, 8], "Java": [9, 10]}
        l3 = Lecturer("E", "F")
        l3.grades = {"C++": [5, 5]}  # без Python
        return [l1, l2, l3]

    def test_avg_existing_course(self, lecturers):
        """Средняя по курсу, который есть у нескольких лекторов."""
        result = avg_lecturers_grade(lecturers, "Python")
        # l1: 8,9; l2: 7,8 => всего 4 оценки, средняя = (8+9+7+8)/4 = 8.0
        assert result == 8.0

    def test_avg_course_one_lecturer(self, lecturers):
        """Курс только у одного лектора."""
        result = avg_lecturers_grade(lecturers, "Java")
        # l1: 6,7; l2: 9,10 => средняя = (6+7+9+10)/4 = 8.0
        assert result == 8.0

    def test_avg_course_no_lecturers(self, lecturers):
        """Курс отсутствует у всех лекторов."""
        result = avg_lecturers_grade(lecturers, "Git")
        assert result == 0.0

    def test_avg_empty_list(self):
        result = avg_lecturers_grade([], "Python")
        assert result == 0.0