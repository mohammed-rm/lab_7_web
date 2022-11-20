import cgi

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")

USER_NAME = "admin"
PASSWORD = "password"

if form.getvalue("user_name") is not None and form.getvalue("password") is not None:
    if form.getvalue("user_name") == USER_NAME and form.getvalue("password") == PASSWORD:
        print("<META HTTP-EQUIV='refresh' CONTENT='0;URL=http://localhost:8000/welcome.py'>")
    else:
        print("Wrong user name or password")
else:
    print("Please enter your user name and password")

login = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>Login page</title>
</head>
<body>
<form method="post" action="login.py">
<input type="text" name="user_name" placeholder="Your name"/>
<input type="password" name="password" placeholder="Your password"/>
<input type="submit" value="Submit", name="send" value="Send login information">
</form>
</body>
</html>
"""

print(login)
