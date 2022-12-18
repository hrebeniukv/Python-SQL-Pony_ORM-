from utilities.base_mongo import BaseMongo


class Teacher(BaseMongo):
    def __init__(self):
        super().__init__()
        self.collection_name = 'Teachers'

    def add_new_teacher(self, teacher_data: dict):
        self.add_new_data(self.collection_name, teacher_data)

    def add_new_teachers(self, teachers_data: list):
        self.add_new_data(self.collection_name, teachers_data)

    def show_all_teachers(self):
        teachers = self.find_documents(self.collection_name)
        return list(teachers)

    def find_teacher_by_name(self, name):
        teacher = self.find_document(self.collection_name, {"name": name})
        return teacher

    def find_teachers_by_subject(self, subject):
        teachers = self.find_documents(self.collection_name, {"subject": subject})
        return list(teachers)

    def get_total_salary(self):
        teachers_list = self.find_documents(self.collection_name)
        total_salary = sum([teacher['salary'] for teacher in teachers_list])
        return total_salary

    def find_teacher_by_biggest_salary(self):
        out_put_options = {'_id': 0, }
        teachers_list = self.find_documents(self.collection_name, out_put_options=out_put_options)
        return teachers_list.sort('salary', -1).limit(1)

    def remove_teachers_wih_age(self, age):
        self.delete_documents(self.collection_name, {"age": age})

    def remove_teacher_name(self, name):
        self.delete_document(self.collection_name, {"name": name})

    def increase_the_salary_for_all_teachers_on(self, percent_increase):
        teachers = self.find_documents(self.collection_name)
        for teacher in teachers:
            update = {'_id': teacher['_id']}
            teacher['salary'] += teacher['salary'] * percent_increase / 100
            query = [{'$set': {'salary': teacher['salary']}}]
            self.update_document(query, self.collection_name, update)

    def drop_collections(self):
        self.delete_collection(self.collection_name)
