import requests

# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# params = {
#     "url": "https://www.linkedin.com/in/akhilsanker/"
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)


res = requests.get(
    "https://gist.githubusercontent.com/akhilmedvolt/52776969afccb8331a7749364f9a49cb/raw/0360cc5a1ac899db8f736fe6b0162bbede71b3b5/akhil-macro.json"
)
