groupmates = [
    {
        "name": "Юрий",
        "surname": "Макарченков",
        "exams": ["ВВиТ", "АиГ", "Философия"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Полина",
        "surname": "Титова",
        "exams": ["ВВиТ", "ВышМат", "История"],
        "marks": [3, 5, 4]
    },
    {
        "name": "Олег",
        "surname": "Нечаев",
        "exams": ["ВВиТ", "АиГ", "Философия"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Артем",
        "surname": "Усачев",
        "exams": ["ВВиТ", "АиГ", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Максим",
        "surname": "Хренов",
        "exams": ["ВВиТ", "ВышМат", "История"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Арсений",
        "surname": "Дрейман",
        "exams": ["ВВиТ", "ВышМат", "История"],
        "marks": [4, 3, 5]
    }
]
a = float(input("Наименьший средний балл:"))

def print_students_above_a (students,a):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        summ=0
        for i in student["marks"]:
            summ+=i
            avg=summ/3
        if a<=avg:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students_above_a(groupmates,a)
