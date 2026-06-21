class Mentor:
    """
    Базовый класс для всех наставников (лекторов и проверяющих).

    Содержит общие атрибуты: имя, фамилию и список курсов, к которым прикреплён наставник.

    Attributes:
        name (str): Имя наставника.
        surname (str): Фамилия наставника.
        courses_attached (list): Список названий курсов, закреплённых за наставником.
    """

    def __init__(self, name, surname):
        """
        Инициализация наставника.

        Args:
            name (str): Имя.
            surname (str): Фамилия.
        """
         
        self.name = name
        self.surname = surname
        self.courses_attached = []    

class Lecturer(Mentor):
    """
    Класс лектора, наследующий от Mentor.

    Дополнительно хранит оценки за лекции, полученные от студентов,
    и предоставляет методы для расчёта средней оценки и сравнения лекторов.

    Attributes:
        name (str): Имя.
        surname (str): Фамилия.
        courses_attached (list): Список курсов, которые ведёт лектор.
        grades (dict): Словарь оценок за лекции, где ключ — название курса,
                       значение — список числовых оценок (int).
    """    

    def __init__(self, name, surname):
        """
        Инициализация лектора.

        Args:
            name (str): Имя.
            surname (str): Фамилия.            
        """
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        """
        Вычисляет среднюю оценку лектора за все лекции по всем курсам.

        Returns:
            float: Среднее арифметическое всех оценок. Возвращает 0, если оценок нет.
        """

        if len(self.grades) == 0:
            return 0
        else:
            grades_of_lecturer = list()
            for course in self.grades:                
                grades_of_lecturer.extend(self.grades[course])
        if len(grades_of_lecturer) != 0:
            return sum(grades_of_lecturer)/len(grades_of_lecturer)
        else:
            return 0
    
    def __eq__(self, other):
        """
        Перегружает оператор == для сравнения лекторов по средней оценке.

        Args:
            other (Lecturer): Другой лектор.

        Returns:
            bool: True, если средние оценки равны.
        """
         
        return self.average_grade() == other.average_grade()
        
    def __lt__(self, other):
        """
        Перегружает оператор < для сравнения лекторов по средней оценке.

        Args:
            other (Lecturer): Другой лектор.

        Returns:
            bool: True, если средняя оценка текущего лектора меньше.
        """

        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        """
        Перегружает оператор > для сравнения лекторов по средней оценке.

        Args:
            other (Lecturer): Другой лектор.

        Returns:
            bool: True, если средняя оценка текущего лектора больше.
        """

        return self.average_grade() > other.average_grade()

    def __str__(self):
        """
        Возвращает строковое представление лектора в формате:
        Имя: <name>
        Фамилия: <surname>
        Средняя оценка за лекции: <avg>

        Returns:
            str: Отформатированная строка.
        """

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

class Reviewer(Mentor):
    """
    Класс проверяющего (эксперта), наследующий от Mentor.

    Предоставляет метод для выставления оценок студентам за домашние задания.

    Attributes:
        name (str): Имя.
        surname (str): Фамилия.
        courses_attached (list): Список курсов, которые проверяет эксперт.
    """

    def __init__(self, name, surname):
        """
        Инициализация проверяющего.

        Args:
            name (str): Имя.
            surname (str): Фамилия.
        """

        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        """
        Выставляет оценку студенту за домашнее задание по указанному курсу.

        Оценка засчитывается только если:
        - переданный объект является экземпляром класса Student,
        - курс присутствует в списке закреплённых курсов проверяющего (courses_attached),
        - курс присутствует в списке текущих курсов студента (courses_in_progress).

        Args:
            student (Student): Объект студента, которому ставится оценка.
            course (str): Название курса.
            grade (int): Оценка (предполагается 10-балльная шкала, но проверка не выполняется).

        Returns:
            None, если оценка успешно добавлена.
            str: Сообщение 'Ошибка', если условия не выполнены.

        Note:
            Оценки сохраняются в словаре student.grades, где ключ — курс, значение — список оценок.
            В отличие от rate_lecture, здесь нет проверки на диапазон оценки.
        """
        from src.oop_homework.students import Student

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        """
        Возвращает строковое представление проверяющего в формате:
        Имя: <name>
        Фамилия: <surname>

        Returns:
            str: Отформатированная строка.
        """
        return f'Имя: {self.name}\nФамилия: {self.surname}'
