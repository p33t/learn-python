import xml.etree.ElementTree as ET
import os.path

body = ET.parse('xml-sample.xml').getroot().find('body')

filenames = []
for playlist in body.findall('playlist'):
    video = playlist.find('video')
    src = video.attrib.get('src')
    filename = src.partition(':')[2]
    assert filename != '', 'No file found in video src "' + src + "'"
    filenames.append(filename)

print('Checking ' + str(len(filenames)) + ' files...')

missingFileCount = 0
for filename in filenames:
    if not os.path.isfile(filename):
        missingFileCount += 1
        print('Missing file: ' + filename)

assert missingFileCount == 0, 'There are ' + str(missingFileCount) + ' missing files'

print('done.')

