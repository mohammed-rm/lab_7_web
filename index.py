import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

if form.getvalue("submited_name") is not None:
    with open("data/submited_names", "a") as file:
        file.write(form.getvalue("submited_name"))
        file.write("\n")
    print(f"Bienvenue {form.getvalue('submited_name')}")

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>My Program</title>
</head>
<body>
<form method="post" action="index.py">
<input type="text" name="submited_name" placeholder="Your name"/>
<input type="submit" value="Submit", name="send" value="Send information to server">
</form>
</body>
</html>
"""

print(html)
