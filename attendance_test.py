def test_mark_attendance():
    student_id = "STU101"
    status = "Present"

    if student_id != "" and status in ["Present", "Absent"]:
        print("PASS: Attendance data is valid")
    else:
        print("FAIL: Attendance data is invalid")


def test_empty_student_id():
    student_id = ""

    if student_id == "":
        print("PASS: Empty student ID detected")
    else:
        print("FAIL: Empty student ID test")


test_mark_attendance()
test_empty_student_id()