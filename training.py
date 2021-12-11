import argparse
import json
from json2xml import json2xml
from json2xml.utils import readfromstring

def get_rooms_students(file_students, file_rooms, format):
    results = {}

    with open(file_students, "r", encoding="utf8") as read_file:
        students = json.load(read_file)

    with open(file_rooms, "r", encoding="utf8") as read_file:
        rooms = json.load(read_file)

    for room in rooms:
        results.setdefault(("Room " + str(room["id"])), [])

    # O(N * M) solution
    # for k, v in results.items():
    #     for student in students:
    #         if k == student['room']:
    #             v.append(student['id'])

    # O(N + M) solution
    for student in students:
        student_id = student["id"]
        room_id = student["room"]
        results["Room " + str(room_id)].append({"Student": student_id})

    data_in_json = json.dumps(results, indent=4)

    results_file_name = ""
    data_to_write = None
    if format.lower() == "json":
        data_to_write = data_in_json
        results_file_name = "results.json"
    elif format.lower() == "xml":
        data_in_xml = readfromstring(data_in_json)
        data_to_write = json2xml.Json2xml(data_in_xml).to_xml()
        results_file_name = "results.xml"

    with open(results_file_name, "w", encoding="utf8") as write_file:
        write_file.write(data_to_write)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert json to json or xml")
    parser.add_argument("-r", help="Path to JSON file with rooms")
    parser.add_argument("-s", help="Path to JSON file with students")
    parser.add_argument("-f", help="Format for the output file JSON or XML")
    args = parser.parse_args()

    get_rooms_students(args.s, args.r, args.f)
