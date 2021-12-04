import json

class StudentsGetter:
    @staticmethod
    def get_rooms_students(file_students, file_rooms, file_results):
        results = {}
        with open(file_students, "r", encoding='utf8') as read_file:
            students = json.load(read_file)

        with open(file_rooms, "r", encoding='utf8') as read_file:
            rooms = json.load(read_file)

        for room in rooms:
            results.setdefault(room['id'], [])

        # O(N * M) solution
        # for k, v in results.items():
        #     for student in students:
        #         if k == student['room']:
        #             v.append(student['id'])

        # O(N + M) solution
        for student in students:
            results[student['room']].append(student['id'])

        with open(file_results, "w", encoding='utf8') as write_file:
            json.dump(results, write_file, indent=4)


StudentsGetter.get_rooms_students('students.json', 'rooms.json', 'results.json')
