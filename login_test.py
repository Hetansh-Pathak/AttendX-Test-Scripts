def test_valid_login():
    username = "student123"
    password = "Test@123"

    if username == "student123" and password == "Test@123":
        print("PASS: Valid login test")
    else:
        print("FAIL: Valid login test")


def test_empty_login():
    username = ""
    password = ""

    if username == "" and password == "":
        print("PASS: Empty login fields detected")
    else:
        print("FAIL: Empty login test")


test_valid_login()
test_empty_login()
print("Login test execution completed.")