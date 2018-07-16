'''
from github import Github

g = Github("b678440c02e85ae287d3ec8ececedf4f4c208920")

repo = g.get_user().get_repo("vehiclecounting")

print(repo)


for files in repo.get_file_contents():
    print(files)


for repo in g.get_user().get_repos():
    print(repo.name)
'''
'''
import requests

#r = requests.get('https://api.github.com/users/yilmazedis', auth=('ylmazedis@gmail.com', 'github1994'))

payload = "{\r\n  \"name\": \"Hello-World_2\",\r\n  \"description\": " \
          "\"This is your first repository\",\r\n  \"homepage\": " \
    "\"https://github.com\",\r\n  \"private\": false,\r\n  \"has_issues\": true,\r\n  \"has_projects\": true,\r\n  " \
          "\"has_wiki\": true\r\n}"


r = requests.post("https://api.github.com/user/repos", data=payload, auth=('ylmazedis@gmail.com', 'github1994'))

print(r.status_code)
print(r.json())
print(r.headers['content-type'])

'''

'''
payload = "{\r\n  \"name\": \"Hello-World_2\",\r\n  \"description\": " \
          "\"This is your first repository\",\r\n  \"homepage\": " \
    "\"https://github.com\",\r\n  \"private\": false,\r\n  \"has_issues\": true,\r\n  \"has_projects\": true,\r\n  " \
          "\"has_wiki\": true\r\n}"

r = requests.post("https://api.github.com/user/repos", data=payload, auth=('ylmazedis@gmail.com', 'github1994'))
'''
'''
import pybase64
import requests
import json

url_api = 'https://api.github.com/repos/yilmazedis/newRepository/contents/'
access_token = 'access_token b678440c02e85ae287d3ec8ececedf4f4c208920'


def find_string_in_github(str):

    r_repo = requests.get(url_api, headers={'Authorization': access_token})
    list = []
    for i in range(len(r_repo.json())):
        repo_name = json.loads(json.dumps(r_repo.json()[i]))["name"]
        if repo_name == ".gitignore":
            continue
        print(repo_name)

        r_name = requests.get(url_api + repo_name,headers={'Authorization': access_token})

        resp_dict = json.loads(json.dumps(r_name.json()))

        resp_string = pybase64.standard_b64decode(resp_dict["content"]).decode("utf-8")

        if resp_string.find(str) != -1:
            list.append([[repo_name], [resp_dict["sha"]]])

    return list


list = find_string_in_github("units")

print(*list,sep='\n')
'''
'''

r = requests.get('https://api.github.com/repos/yilmazedis/newRepository/contents/my-new-file',
                 headers={'Authorization': 'access_token b678440c02e85ae287d3ec8ececedf4f4c208920'})

resp_dict = json.loads(json.dumps(r.json()))


resp_string = pybase64.standard_b64decode(resp_dict["content"]).decode("utf-8")

print(resp_string.find("fixes"))


print(r.status_code)
#print(r.json())
print(r.headers['content-type'])

'''
'''
from github import Github

new_repo = "newRepository"
g = Github("b678440c02e85ae287d3ec8ececedf4f4c208920")
user = g.get_user()

repo = g.get_user().get_repo(new_repo)
print(repo)

## first parameter is the path
## Commit comment
## 3. parameter is content of the file
file = repo.create_file("/path.txt", "initial commit", "content\n second line")
print(file)
'''
'''
from github import Github

new_repo = "newRepository"
g = Github("b678440c02e85ae287d3ec8ececedf4f4c208920")
user = g.get_user()

repo = g.get_user().get_repo(new_repo)
print(repo)

file = repo.get_file_contents("/path.txt")

print(file)

file_content = "To protect your rights, we need to prevent others from denying you \
these rights or asking you to surrender the rights.  Therefore, you have\
certain responsibilities if you distribute copies of the software, or if\
you modify it: responsibilities to respect the freedom of others\
For example, if you distribute copies of such a program, whether\
gratis or for a fee, you must pass on to the recipients the same\
freedoms that you received.  You must make sure that they, too, receive\
or can get the source code.  And you must show them these terms so they\
know their rights."

# update
repo.update_file("/path.txt", "your_commit_message", file_content, file.sha)
'''
import pybase64

string_base64 = b'i have tried to add some data to my file'
print(pybase64.standard_b64encode(string_base64))



