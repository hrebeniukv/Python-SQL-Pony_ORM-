from db_collections.teacher_collection import Teacher

Teacher().add_new_teacher({'name': "Tom", "age": 36, "subject": "history", "salary": 6800})
Teacher().add_new_teacher({'name': "James", "age": 28, "subject": "biology", "salary": 4600})
Teacher().add_new_teachers(
    [{'name': "Mery", "age": 23, "subject": "geography", "salary": 2950},
    {'name': "Agata", "age": 68, "subject": "biology", "salary": 5300},
    {'name': "James", "age": 55, "subject": "history", "salary": 5100},
    {'name': "Bart", "age": 39, "subject": "geography", "salary": 5000},
    {'name': "Ines", "age": 64, "subject": "math", "salary": 4300},
    {'name': "Marlen", "age": 27, "subject": "music", "salary": 2800},
    {'name': "Claudia", "age": 34, "subject": "math", "salary": 3900}])

[print(teacher) for teacher in Teacher().show_all_teachers()]

Teacher().increase_the_salary_for_all_teachers_on(20)
[print(teacher) for teacher in Teacher().show_all_teachers()]

[print(teacher) for teacher in Teacher().find_teacher_by_biggest_salary()]

Teacher().remove_teachers_wih_age(68)
[print(teacher) for teacher in Teacher().show_all_teachers()]

print(total_salary := Teacher().get_total_salary())

[print(teacher) for teacher in Teacher().find_teachers_by_subject('geography')]

print(teaher := Teacher().find_teacher_by_name('Marlen'))


# Teacher().drop_collections()