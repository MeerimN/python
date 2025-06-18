import requests
import pprint

url = "https://backend.akumotechnology.com/api/students/me/certificates"
cookies = {"access_token_cookie": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYXJ5bnVyYmVrb3ZhQGdtYWlsLmNvbSIsImV4cCI6MTc1MDEyNjcxN30.k-hFFwRMhg7ALqM2ehOJNrspk_yC4qZkFLq047inlh0"}
about_me = requests.get(url, cookies=cookies)
print((certificates.json()))