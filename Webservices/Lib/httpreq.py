'''
http request
'''

import json
import requests
# header = {'content-type': 'application/json' }
def httprequest(method, url, Headers, Params=None, Payload=None, Verify=False):

    res = None
    if Payload !=None:
        Payload = json.dumps(Payload)

    print ("Headers :" + str(Headers))
    print ("URL : " + str(url))
    print ("method : " + str(method))
    print ("payload :" + str(Payload))
    print ("params :" + str(Params))
    print ("SSL verify :" + str(Verify))

    try:
        if (method == "POST" or method == 'post'):
            res =requests.post(url, headers=Headers, data=Payload, params=Params, verify=Verify, timeout=60)
        elif (method == "PUT" or method == 'put'):
            res =requests.put(url, headers=Headers, data=Payload, params=Params, verify=Verify, timeout=60)
        elif (method == "DELETE" or method == 'delete'):
            res = requests.delete(url, headers=Headers, data=Payload, params=Params, verify=Verify, timeout=60)
        elif (method == "GET" or method == 'get'):
            res =requests.get(url, headers=Headers, data=Payload, params=Params, verify=Verify, timeout=60)
        else:
            print ("Invalid url")
    except Exception as e:
        print (method, e)
    return res.json()

# if __name__ == "__main__":
#
#     method = 'get'
#     url = 'https://api.github.com/search/repositories'
#     headers = {'content_typ': 'application/json'}
#     params = {'q': 'requests+language:python'}
#     response = httprequest(method, url, headers, params)
#
#     # response.encoding = 'utf-8'  # Optional: requests infers this internally
#     # print (response.text).encode('utf-8')
#
#     json_response = response.json()
#     repository = json_response['items'][0]
#     for item in repository:
#         if str(item) == 'issues_url':
#             print str(repository[item])
#         else:
#             continue
