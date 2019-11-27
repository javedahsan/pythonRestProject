'''
test Web Services with unittest framework
'''

import unittest
from Webservices.CommonAPI.findLibraries import getLibraries
import time


class testwebservices(unittest.TestCase):

    findlibs = getLibraries()
    findlibs.getConfig()



    def test_01_get_repositories(self):
        detailUrl = []
        json_response = self.findlibs.get_repository('get')

        time.sleep(10)
        repository = json_response['items'][0]

        for item in repository:
            if str(item) != 'issues_url':
                continue
            else:
                detailUrl = str(repository[item]).split("{")
        self.findlibs.setdetailUrl(detailUrl[0])
        print "TC1:", detailUrl
        self.assertEqual(detailUrl[0], 'https://api.github.com/repos/spyoungtech/grequests/issues')

    def test_02_get_repositoryIssuesNumber(self):
        issue_num = []
        print "URLTC2 ", self.findlibs.getdetailUrl()
        # Get list of all issues urls
        json_response = self.findlibs.get_detailRepo('get', self.findlibs.detailUrl)

        # json_response = json.dumps(json_response)

        for item in json_response:
            issue_num.append(item['number'])
        issueNm = max(issue_num)
        self.findlibs.setIssueNumber(issueNm)

        self.assertGreaterEqual(issueNm, 0)


    # def tearDown(self):
    #      del self.findlibs


if __name__ == "__main__":
    unittest.main()