import requests

payload = "{\r\n  \"name\": \"Hello-World_2\",\r\n  \"description\": " \
          "\"This is your first repository\",\r\n  \"homepage\": " \
    "\"https://github.com\",\r\n  \"private\": false,\r\n  \"has_issues\": true,\r\n  \"has_projects\": true,\r\n  " \
          "\"has_wiki\": true\r\n}"


r = requests.post("https://api.github.com/user/repos", data=payload, auth=('user_id', 'password'))

print(r.status_code)
print(r.json())
print(r.headers['content-type'])