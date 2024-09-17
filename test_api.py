from github import Github


username = input("Enter username: ")
token = input("Enter token: ")
repo_name = input("Enter repository name: ")

git = Github(token)

user = git.get_user()
new_repo = user.create_repo(repo_name)

repo = git.get_repo(f"{username}/{repo_name}")
try:
    repo = git.get_repo(f"{username}/{repo_name}")
    print(f"Repository '{repo_name}' created successfully")
except:
    raise Exception("Repository not created")

repo.delete()
try:
    repo = git.get_repo(f"{username}/{repo_name}")
    raise Exception(f"Repository '{repo_name}' not deleted")
except:
    print(f"Repository '{repo_name}' deleted successfully")
