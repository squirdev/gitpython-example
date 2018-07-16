from github import Github

new_repo = "newRepository"
g = Github("access_token")
user = g.get_user()

repo = g.get_user().get_repo(new_repo)
print(repo)

## first parameter is the path
## Commit comment
## 3. parameter is content of the file
file = repo.create_file("/path.txt", "initial commit", "content\nsecond content")
print(file)