'''
findLibraries class to access all web api
'''

import os, time
import json

from Webservices.Lib.httpreq import httprequest
from Webservices.Lib.apiconfigparser import apicfgparser
from Webservices.Lib.readXmlFile import writeOutputFile

dir_path = os.path.dirname(os.path.realpath(__file__))


class getLibraries(object):
    def __init__(self):
        print("Test Execution in progress")
        self.result = ''
        self.expected = ''
        self.status = ''
        self.response = ''
        self.outputresponse = ''
        self.repoid = ''
        cwd = os.path.join(dir_path, '../Config/')
        configfile = (cwd + 'apiconfig.cfg')
        self.headers = ''
        self.url = ''
        self.params = ''
        self.detailUrl = ''
        self.issueNumber = ''

    def setdetailUrl(self, detailUrl):
        self.detailUrl = detailUrl

    def getdetailUrl(self):
        return self.detailUrl

    def setIssueNumber(self, issueNum):
        self.issueNumber = issueNum

    def getIssueNumber(self):
        return self.issueNumber

    def getConfig(self):
        # self.headers = apicfgparser("Header", "api_header")
        self.headers = {'content-type': 'application/json'}
        self.url = apicfgparser("urls", "url_python")
        # self.params = apicfgparser("Params", "url_params")
        self.params = {'q': 'requests+language:python'}

    def get_repository(self, method):
        # method = 'get'
        # url = 'https://api.github.com/search/repositories'
        headers = {'content-type': 'application/json'}
        params = {'q': 'requests+language:python'}
        # print (self.url, ' ',  self.headers, ' ', self.params)
        response = httprequest(method, self.url, headers, params)
        return response

    def get_detailRepo(self, method, url ):
            response = httprequest(method, url, self.headers)
            return response

    def readXml_file(self):
        response = writeOutputFile()
        print(response.attrib['Version_Major'], response.attrib['Version_Minor'], response.attrib['Creation_Date'])
        return response.attrib['Version_Major'], response.attrib['Version_Minor']

#     def readCSV_file
#     def readJson_file
#     def readText_file
#     def readXls_file


# if __name__ == "__main__":
#     detailUrl = []
#     issue_num = []
#     findlibs = findLibraries()
#     findlibs.getConfig()
#     json_response = findlibs.get_repository('get')
#     time.sleep(10)
#
#
#     repository = json_response['items'][0]
#
#     # get issues url and ignore the rest of url
#     for item in repository:
#         if str(item) != 'issues_url':
#             continue
#         else:
#             print str(repository[item])
#             detailUrl = str(repository[item]).split("{")
#
#     # Get list of all issues urls
#     json_response = findlibs.get_detailRepo('get', detailUrl[0])
#     # json_response = json.dumps(json_response)
#     print 'Detail:', type(json_response)
#
#     for item in json_response:
#         issue_num.append(item['number'])
#
#     issueNo = max(issue_num)  # type: object
#
#     # Get list of all issues urls
#     json_response = findlibs.get_detailRepo('get', detailUrl[0]+'/'+str(issueNo))
#     print 'Detail2:', type(json_response)
#     for key, value in json_response.items():
#         print key, ' :: ', value
#
#     #  Read XML file
#     MajorVersion, MinorVersion = findlibs.readXml_file()