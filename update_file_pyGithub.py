from github import Github

new_repo = "newRepository"
g = Github("access_token")
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