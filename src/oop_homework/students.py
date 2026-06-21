class Student:
    """
    Класс, представляющий студента учебного заведения.

    Хранит личную информацию, список завершённых и текущих курсов,
    а также оценки за домашние задания, полученные от проверяющих (Reviewer).

    Attributes:
        name (str): Имя студента.
        surname (str): Фамилия студента.
        gender (str): Пол студента (например, 'М' или 'Ж').
        finished_courses (list): Список названий завершённых курсов.
        courses_in_progress (list): Список названий курсов, изучаемых в данный момент.
        grades (dict): Словарь, где ключ — название курса, значение — список числовых оценок (int) за домашние задания.
    """
     
    def __init__(self, name, surname, gender):
        """
        Инициализация студента.

        Args:
            name (str): Имя.
            surname (str): Фамилия.
            gender (str): Пол.
        """
          
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        """
        Добавляет курс в список завершённых.

        Args: course_name (str): Название курса.
        """
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        """
        Выставляет оценку лектору за прочитанный курс.

        Оценка засчитывается только если:
        - переданный объект является экземпляром класса Lecturer,
        - курс присутствует в списке закреплённых курсов лектора (courses_attached),
        - курс присутствует в списке текущих курсов студента (courses_in_progress).

        Args:
            lecturer (Lecturer): Объект лектора, которому ставится оценка.
            course (str): Название курса.
            grade (int): Оценка по 10-балльной шкале (от 1 до 10).

        Returns:
            None, если оценка успешно добавлена.
            str: Сообщение об ошибке, если условия не выполнены или оценка вне допустимого диапазона.

        Note:
            Оценки сохраняются в словаре lecturer.grades, где ключ — курс, значение — список оценок.
        """

        from src.oop_homework.mentors import Lecturer   # <--- ДОБАВЬТЕ ЭТУ СТРОКУ
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade < 1 or grade > 10:
                return 'Ошибка: оценка не соответствует 10-балльной системе'
            else:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self):
        """
        Вычисляет среднюю оценку студента за все домашние задания по всем курсам.

        Returns:
            float: Среднее арифметическое всех оценок. Возвращает 0, если оценок нет.
        """

        if len(self.grades) == 0:
            return 0
        else:
            grades_of_student = list()
            for course in self.grades:                
                grades_of_student.extend(self.grades[course])
        if len(grades_of_student) != 0:
            return sum(grades_of_student)/len(grades_of_student)
        else:
            return 0
    
    def __eq__(self, other):
        """
        Перегружает оператор == для сравнения студентов по средней оценке.

        Args:
            other (Student): Другой студент для сравнения.

        Returns:
            bool: True, если средние оценки равны.
        """

        return self.average_grade() == other.average_grade()
        
    def __lt__(self, other):     
        """
        Перегружает оператор < для сравнения студентов по средней оценке.

        Args:
            other (Student): Другой студент.

        Returns:
            bool: True, если средняя оценка текущего студента меньше.
        """

        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        """
        Перегружает оператор > для сравнения студентов по средней оценке.

        Args:
            other (Student): Другой студент.

        Returns:
            bool: True, если средняя оценка текущего студента больше.
        """

        return self.average_grade() > other.average_grade()

    def __str__(self):
        """
        Возвращает строковое представление студента в формате:
        Имя: <name>
        Фамилия: <surname>
        Средняя оценка за домашние задания: <avg>
        Курсы в процессе изучения: <course1, course2, ...>
        Завершенные курсы: <course1, course2, ...>

        Returns:
            str: Отформатированная строка.
        """
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'        
