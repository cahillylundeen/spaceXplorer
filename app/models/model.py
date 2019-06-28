import requests
# next launch
def next_launch():
   url = 'https://api.spacexdata.com/v3/launches/next'
   response = requests.get(url)
   if response.status_code == 200:
      # print(response.content)
      return response.json()
   elif response.status_code == 404:
      print('Not found!')
   return dict({ 'data': 'none' })

# latest launch
def last_launch():
   url = 'https://api.spacexdata.com/v3/launches/latest'
   response = requests.get(url)
   if response.status_code == 200:
      # print(response.content)
      return response.json()
   elif response.status_code == 404:
      print('Not found!')
   return dict({ 'data': 'none' })

def past_launches():
   url = 'https://api.spacexdata.com/v3/launches/past'
   response = requests.get(url)
   if response.status_code == 200:
      # print(response.content)
      return response.json()
   elif response.status_code == 404:
      print('Not found!')
   return dict({ 'data': 'none' })
   
import requests

def flights_search(term='drake'):

    url = 'https://api.spacexdata.com/v3/launches'
    print(url)
    # response = requests.get(url+term)
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.content)
        return response.json()
    elif response.status_code == 404:
        print('Not found!')
    return dict({ 'data': 'none' })