'''
api configuration
'''

import os
import configparser

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "../Config/")


def apicfgparser (section,key):
    configfile = (file_path + 'apiconfiguration.cfg')

    #     initiate configparsre object
    config = configparser.ConfigParser()
    # open file with object
    config.readfp(open(configfile))
    # get properties
    value = config.get(section,key)
    return value


if __name__ == "__main__":
    print dir_path, " ", file_path


    print apicfgparser("Header", "api_header")
    print apicfgparser("urls", "url_python")
