'''
Read xml file

'''

import sys, os
import xml.etree.ElementTree as ET

file_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(file_path, '../data/inputFolder/')
input_file = (input_path + 'episode.xml')

output_path = os.path.join(file_path, '../data/outputFolder/')
output_file = (output_path + 'episode.xml')

def updateVersion(param1, param2):
    num1 = int(param1)
    num2 = int(param2)

    num1+= 1
    num2+= 1
    return str(num1), str(num2)

def readInputFile():
    # file_path = os.path.dirname(os.path.realpath(__file__))
    # cwd = os.path.join(file_path, '../data/inputFolder/')
    # inputfile = (cwd + 'episode.xml')

    tree = ET.parse(input_file)

    root = tree.getroot()
    # print root

    # 1. get all child tag and attrib
    # for item in root.findall('./Asset/Metadata'):
    #    print type(item)
    #    for child in item:
    #         print 'childTag:' , child.tag, "ChildAttrib:", child.attrib

    # 2. get all tag from root
    # result = [elem.tag for elem in root.iter()]
    # print result

    # 3. Get whole document if we more ET to toString()
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))

    # 4. Now finding particular element by iter()
    # for amsElem in root.iter("AMS"):
    #     # get All attributes
    #     print amsElem.attrib[]
    #
    #     # get Asset_id attribute
    #     print amsElem.attrib['Asset_ID']

    # 5. get the text
    # for appElem in root.iter("App_Data"):
    #     print appElem.attrib

    # 6. def  xpath with given attributes
    # for movie in root.findall("./Asset/Asset/Metadata/App_Data/[@Value='box cover']"):
    #     print(movie.attrib)

    # 7. Get parent element by ...
    # for movie in root.findall("./Asset/Asset/Metadata/App_Data/[@Value='box cover']..."):
    #     print(movie.tag ,' ', movie.attrib)

    # 8. modify xml find 'box cover' and and update with box_cover
    # movie = root.find("./Asset/Asset/Metadata/App_Data/[@Value='box cover']")
    movie = root.find("./Asset/Asset/Metadata/AMS")

    # print(movie.attrib['Version_Major'], movie.attrib['Version_Minor'], movie.attrib['Creation_Date'])

    majorVer = movie.attrib['Version_Major']
    minorVer = movie.attrib['Version_Minor']

    majorVer, minorVer = updateVersion(majorVer, minorVer)

    movie.attrib['Version_Major'] = majorVer
    movie.attrib['Version_Minor'] = minorVer

    # movie.attrib["Value"] = "box_cover"

    # print(movie.attrib)
    return tree


def writeOutputFile():
    # file_path = os.path.dirname(os.path.realpath(__file__))
    # cwd = os.path.join(file_path, '../data/inputFolder/')
    # inputfile = (cwd + 'episode.xml')
    result = readInputFile()

    result.write(output_file)

    tree = ET.parse(output_file)

    root = tree.getroot()
    # print "Write folder"
    # print root

    # movie = root.find("./Asset/Asset/Metadata/AMS/[@Value='box_cover']")

    movie = root.find("./Asset/Asset/Metadata/AMS")
    # print(movie.attrib['Version_Major'], movie.attrib['Version_Minor'], movie.attrib['Creation_Date'])

    return movie

# if __name__ =="__main__":

    # result = readInputFile()
    # writeOutputFile(result)
