import base64
import os
from github import Github
from pprint import pprint


token = input("Enter token: ")
username = input("Enter username: ")

git = Github(token)
repo = git.get_repo(f"{username}/E2E_UI")

repo.create_file("test.txt", "commit message", "content of the file")

contents = repo.get_contents("test.txt")
repo.delete_file(contents.path, "remove test.txt", contents.sha)
