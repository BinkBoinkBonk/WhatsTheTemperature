import requests, webbrowser
from bs4 import BeautifulSoup
from uszipcode import SearchEngine

#Note to self, Website for webscraping uses zipcode only so no need for state and city
def main():
  state2 = input("What state do you live in?\n")
  city2 = input("What city do you live in?\n")
  search = SearchEngine(simple_zipcode=True)
  res = search.by_city_and_state(city2, state2, zipcode_type='Standard', sort_by='zipcode', ascending=True, returns=5)
  len(res)
  zipcode = res[0]
  zipcode
  city = zipcode.major_city
  state = zipcode.state
  urlend = zipcode.zipcode
  URL = 'https://www.weatherbug.com/weather-forecast/10-day-weather/'+ urlend
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  temp = soup.find(class_='temp').get_text()
  print('The temp right now in ' + city + ', ' + state +' is' + temp)
  main()
main()
# Shameless plug, follow my IG: @im.thomas_
