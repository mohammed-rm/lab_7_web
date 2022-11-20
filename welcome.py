import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>Welcome page</title>
</head>
<body>
<div>
Welcome to your page !
</div>
</body>
</html>
"""
print(html)
