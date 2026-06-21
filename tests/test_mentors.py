# tests/test_mentors.py
import pytest
from src.oop_homework.mentors import Mentor, Lecturer, Reviewer
from src.oop_homework.students import Student


class TestMentor:
    """Тесты базового класса Mentor."""

    def test_init(self):
        mentor = Mentor("Иван", "Петров")
        assert mentor.name == "Иван"
        assert mentor.surname == "Петров"
        assert mentor.courses_attached == []


class TestLecturer:
    """Тесты класса Lecturer."""

    @pytest.fixture
    def lecturer(self):
        return Lecturer("Иван", "Иванов")

    def test_inheritance(self, lecturer):
        """Проверка наследования от Mentor."""
        assert isinstance(lecturer, Mentor)
        assert isinstance(lecturer, Lecturer)

    def test_init(self, lecturer):
        assert lecturer.name == "Иван"
        assert lecturer.surname == "Иванов"
        assert lecturer.courses_attached == []
        assert lecturer.grades == {}

    def test_average_grade_no_grades(self, lecturer):
        assert lecturer.average_grade() == 0

    def test_average_grade_with_grades(self, lecturer):
        lecturer.grades = {"Python": [5, 6], "Java": [7, 8]}
        assert lecturer.average_grade() == (5+6+7+8) / 4

    def test_comparison(self, lecturer):
        l1 = Lecturer("A", "B")
        l1.grades = {"Python": [5, 5]}  # средняя 5
        l2 = Lecturer("C", "D")
        l2.grades = {"Python": [7, 7]}  # средняя 7

        assert l1 < l2
        assert l2 > l1
        assert not l1 == l2

        l3 = Lecturer("E", "F")
        l3.grades = {"Python": [5, 5, 5]}  # тоже 5
        assert l1 == l3

    def test_str(self, lecturer):
        lecturer.grades = {"Python": [7, 8]}
        expected = "Имя: Иван\nФамилия: Иванов\nСредняя оценка за лекции: 7.5"
        assert str(lecturer) == expected


class TestReviewer:
    """Тесты класса Reviewer."""

    @pytest.fixture
    def reviewer(self):
        r = Reviewer("Петр", "Петров")
        r.courses_attached = ["Python", "Java"]
        return r

    @pytest.fixture
    def student(self):
        s = Student("Алёхина", "Ольга", "Ж")
        s.courses_in_progress = ["Python", "Java"]
        return s

    def test_inheritance(self, reviewer):
        assert isinstance(reviewer, Mentor)
        assert isinstance(reviewer, Reviewer)

    def test_init(self, reviewer):
        assert reviewer.name == "Петр"
        assert reviewer.surname == "Петров"
        assert reviewer.courses_attached == ["Python", "Java"]

    def test_rate_hw_success(self, reviewer, student):
        result = reviewer.rate_hw(student, "Python", 9)
        assert result is None
        assert student.grades == {"Python": [9]}

        # Добавляем ещё оценку
        reviewer.rate_hw(student, "Python", 8)
        assert student.grades == {"Python": [9, 8]}

        # Оценка по другому курсу
        reviewer.rate_hw(student, "Java", 7)
        assert student.grades == {"Python": [9, 8], "Java": [7]}

    def test_rate_hw_not_student(self, reviewer):
        """Попытка оценить не-студента."""
        result = reviewer.rate_hw("not a student", "Python", 5)
        assert result == "Ошибка"

    def test_rate_hw_course_not_in_reviewer(self, reviewer, student):
        """Курс не прикреплён к проверяющему."""
        result = reviewer.rate_hw(student, "C++", 5)
        assert result == "Ошибка"
        assert student.grades == {}

    def test_rate_hw_course_not_in_student(self, reviewer, student):
        """Курс не в процессе изучения студента."""
        result = reviewer.rate_hw(student, "Git", 5)
        assert result == "Ошибка"
        assert student.grades == {}

    def test_str(self, reviewer):
        expected = "Имя: Петр\nФамилия: Петров"
        assert str(reviewer) == expected