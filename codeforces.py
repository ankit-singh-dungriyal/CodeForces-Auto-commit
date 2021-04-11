import sys
import os.path
import json
import datetime
from user_details import*

if(os.path.exists('input.txt')):
	sys.stdin= open('input.txt','r')
	sys.stdout=open('output.txt','w')

import requests
from bs4 import BeautifulSoup
import html5lib

# getting problem data and returning in form of dictionary
def add_problems(d):
	tmp_d={}
	tmp_d['id']=d['id']
	tmp_d['contestId']=d['contestId']
	date=datetime.datetime.fromtimestamp(d['creationTimeSeconds'])
	tmp_d['submission_date']=date.strftime('%d/%m/%Y')
	tmp_d['submission_time']=date.strftime('%H:%M:%S')
	tmp_d['problem']=d['problem']['index']+"_"+d['problem']['name']
	tmp_d['concept']=d['problem']['tags']
	tmp_d['url']="https://codeforces.com/contest/"+str(d['contestId'])+"/submission/"+str(d['id'])

	return tmp_d




# using codeforces api
url=" https://codeforces.com/api/user.status?handle="+user_handle+"&from=1&count=100"

r=requests.get(url)
htmlcontent=r.content
# print(htmlcontent)
soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup)

# modifying the string
s=soup.string
s=s[25:-2]
s=s.replace(",{\"id","\n{\"id")

data_list=s.split("\n")
status_list=[]

# putting string in json format

for i in data_list:
	status_list.append(json.loads(i))


problems=[]
curr_date=datetime.datetime.now()
todays_date=str(curr_date.day)+'/'+str(curr_date.month)+'/'+str(curr_date.year)

for d in status_list:
	date=datetime.datetime.fromtimestamp(d['creationTimeSeconds'])
	submission_date=str(date.day)+'/'+str(date.month)+'/'+str(date.year)
	# print(submission_date==todays_date)
	# print(submission_date," ",todays_date)

	# add all those problems which are successfully solved in current date
	if(d['verdict']=='OK' and submission_date==todays_date):
		problems.append(add_problems(d))


def problems_data():
	return problems