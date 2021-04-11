import base64
from github import Github
from user_details import*



g = Github(token)
repo = g.get_user().get_repo(repo_name)


def upload_file(path,commit_message,file_content):
    try:
        repo.create_file(path,commit_message,file_content)
    except:
        print(path+" file already exist ! ")



