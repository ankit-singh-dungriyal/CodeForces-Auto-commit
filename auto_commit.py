import sys
import os.path
from codeforces import problems_data
from github_upload import upload_file
from user_details import*

if(os.path.exists('input.txt')):
	sys.stdin= open('input.txt','r')
	sys.stdout=open('output.txt','w')

import requests
from bs4 import BeautifulSoup
import html5lib


# getting information of the problems
def get_info(d):
	s="/*\n"
	s+="Contest Id: "+str(d['contestId'])+"\n"
	s+="Submission Id: "+str(d['id'])+"\n"
	s+="Date & Time: "+d['submission_date']+" "+d['submission_time']+"\n"
	s+="Tags/Concept used: "+str(d['concept'])+"\n*/\n\n"
	return s

problems=problems_data()

for d in problems:
	url=d['url']
	r=requests.get(url)
	htmlcontent=r.content
	soup=BeautifulSoup(htmlcontent,'html.parser')
	code=soup.find(id='program-source-text').string

	file_content=get_info(d)+code
	commit_message=d['problem']
	path=folder_path+str(d['contestId'])+" - "+d['problem']+".cpp"

	upload_file(path,commit_message,file_content)