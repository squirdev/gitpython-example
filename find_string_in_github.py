import pybase64
import requests
import json

def find_string_in_github(str,file_path,access_token):

    git_url = 'https://api.github.com/repos/' + file_path + '/contents/'

    r_repo = requests.get(git_url,headers={'Authorization': 'access_token ' + access_token})
    list = []
    for i in range(len(r_repo.json())):
        repo_name = json.loads(json.dumps(r_repo.json()[i]))["name"]
        if repo_name == ".gitignore":
            continue
        print(repo_name)

        r_name = requests.get(git_url + repo_name,headers={'Authorization': access_token})

        resp_dict = json.loads(json.dumps(r_name.json()))

        resp_string = pybase64.standard_b64decode(resp_dict["content"]).decode("utf-8")

        if resp_string.find(str) != -1:
            list.append([[repo_name], [resp_dict["sha"]]])

    return list


list = find_string_in_github("units", 'yilmazedis/newRepository', 'b678440c02e85ae287d3ec8ececedf4f4c208920')

print(*list,sep='\n')