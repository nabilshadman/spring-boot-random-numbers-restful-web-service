import requests

from requests.exceptions import HTTPError

try:
    url = "http://localhost:8080/random?bound=5&origin=1&size=100"

    response = requests.get(url)
    json = response.json()
    
    rand_nums = json['numArray']
    sum = 0

    for num in rand_nums:
        print(num)
        sum += num
    
    print("sum of random numbers = ", sum)

except HTTPError as err:
    print(f'HTTP error occurred: {err}')
