# tests/test_students.py
import pytest
from src.oop_homework.students import Student
from src.oop_homework.mentors import Lecturer, Reviewer


class TestStudent:
    """Тесты для класса Student."""

    @pytest.fixture
    def student(self):
        """Создаёт студента с предустановленными курсами."""
        s = Student("Алёхина", "Ольга", "Ж")
        s.courses_in_progress = ["Python", "Java"]
        s.finished_courses = ["C++"]
        return s

    @pytest.fixture
    def lecturer(self):
        """Создаёт лектора с прикреплёнными курсами."""
        l = Lecturer("Иван", "Иванов")
        l.courses_attached = ["Python", "Java"]
        return l

    def test_init(self, student):
        """Проверка инициализации атрибутов."""
        assert student.name == "Алёхина"
        assert student.surname == "Ольга"
        assert student.gender == "Ж"
        assert student.courses_in_progress == ["Python", "Java"]
        assert student.finished_courses == ["C++"]
        assert student.grades == {}

    def test_add_courses(self, student):
        """Проверка добавления завершённого курса."""
        student.add_courses("Git")
        assert "Git" in student.finished_courses

    def test_rate_lecture_success(self, student, lecturer):
        """Успешное выставление оценки лектору."""
        result = student.rate_lecture(lecturer, "Python", 7)
        assert result is None
        assert lecturer.grades == {"Python": [7]}

        # Добавляем ещё одну оценку по тому же курсу
        student.rate_lecture(lecturer, "Python", 9)
        assert lecturer.grades == {"Python": [7, 9]}

    def test_rate_lecture_invalid_grade(self, student, lecturer):
        """Оценка вне диапазона 1-10 вызывает ошибку."""
        result = student.rate_lecture(lecturer, "Python", 0)
        assert result == "Ошибка: оценка не соответствует 10-балльной системе"
        result = student.rate_lecture(lecturer, "Python", 11)
        assert result == "Ошибка: оценка не соответствует 10-балльной системе"
        # Оценки не должны быть добавлены
        assert lecturer.grades == {}

    def test_rate_lecture_not_lecturer(self, student):
        """Попытка оценить не-лектора."""
        reviewer = Reviewer("Петр", "Петров")
        result = student.rate_lecture(reviewer, "Python", 5)
        assert result == "Ошибка"

    def test_rate_lecture_course_not_in_lecturer(self, student, lecturer):
        """Курс не прикреплён к лектору."""
        result = student.rate_lecture(lecturer, "C++", 5)
        assert result == "Ошибка"
        assert lecturer.grades == {}

    def test_rate_lecture_course_not_in_student(self, student, lecturer):
        """Курс не в процессе изучения студентом."""
        result = student.rate_lecture(lecturer, "Git", 5)
        assert result == "Ошибка"
        assert lecturer.grades == {}

    def test_average_grade_no_grades(self, student):
        """Средняя оценка при отсутствии оценок."""
        assert student.average_grade() == 0

    def test_average_grade_with_grades(self, student):
        """Средняя оценка при наличии оценок по нескольким курсам."""
        student.grades = {"Python": [5, 6], "Java": [7, 8]}
        assert student.average_grade() == (5+6+7+8) / 4

    def test_comparison_operators(self, student):
        """Сравнение студентов по средней оценке."""
        s1 = Student("A", "B", "M")
        s1.grades = {"Python": [5, 5]}  # средняя 5
        s2 = Student("C", "D", "M")
        s2.grades = {"Python": [7, 7]}  # средняя 7

        # Принудительно пересчитывать среднюю не нужно, она вычисляется в методах
        # Но для надёжности создадим объекты с уже выставленными оценками

        # Сравниваем: s1 < s2
        assert s1 < s2
        assert s2 > s1
        assert not s1 == s2

        # Создаём третьего с такой же средней, как у s1
        s3 = Student("E", "F", "M")
        s3.grades = {"Python": [5, 5, 5]}  # тоже средняя 5 (15/3=5)
        assert s1 == s3
        assert not s1 < s3
        assert not s1 > s3

    def test_str(self, student):
        """Проверка строкового представления."""
        student.grades = {"Python": [7, 8]}
        expected = (
            "Имя: Алёхина\n"
            "Фамилия: Ольга\n"
            "Средняя оценка за домашние задания: 7.5\n"
            "Курсы в процессе изучения: Python, Java\n"
            "Завершенные курсы: C++"
        )
        assert str(student) == expected