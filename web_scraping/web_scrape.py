import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		points = int(votes[idx].getText().replace(' points', ''))
		print(points)
		hn.append({'title':title, 'links':href})	
	return hn


print(create_custom_hn(links, votes))
