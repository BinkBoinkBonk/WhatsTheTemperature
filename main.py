import requests
from bs4 import BeautifulSoup
from uszipcode import SearchEngine # BIG thanks to Sanhe Hu for uszipcode. With out that it would have been more strainful to get all of this working. His package also includes spell help on the states and cities.

print("This python script will tell you the temperature in the State and City you enter.\n") #This will only work in the United States as the website I have chosen to webscrape uses zipcodes to search for the temperature.

def main():
  state2 = input("What state do you want the temperature of?\n")
  city2 = input("What city do you want the temperature of?\n")
  search = SearchEngine(simple_zipcode=True)
  res = search.by_city_and_state(city2, state2, zipcode_type='Standard', sort_by='zipcode', ascending=True, returns=5)
  len(res)
  try:
    zipcode = res[0]
  except IndexError:
    print("Please type in a valid USA State/City\n")
    main()
  zipcode
  city = zipcode.major_city
  state = zipcode.state
  urlend = zipcode.zipcode
  URL = 'https://weather.com/weather/today/l/'+ urlend
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  temp = soup.find(class_='CurrentConditions--tempValue--3KcTQ').get_text()
  print('\nThe temperature right now in ' + city + ', ' + state +' is ' + temp + "\n")
  main()
main()
# Thanks for taking a look at my code! 