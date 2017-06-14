# need for mac
import subprocess
# need for version
import sys

class Connection:
    def __init__(self, os, version, printOutErrors = True):
        # Default properties
        self.properties = []
        self.os = os
        self.printOutErrors = printOutErrors

        if os == 'osx':
            # Get Wifi Info using Mac

            # Uses command line to get wifi. For more info: https://gist.github.com/keithweaver/00edf356e8194b89ed8d3b7bbead000c
            process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
            out, err = process.communicate()
            process.wait()

            # Output is string split by newlines
            listOfUnformattedAttributes = out.split('\n');

            for strAttr in listOfUnformattedAttributes:
                # Format the string
                # 1. Remove leading and ending whitespaces
                # 2. Split into key value
                # 3. Strip whitespace from value and key
                # 4. Create object for them and add to properties
                if strAttr != '':
                    strAttr = strAttr.strip()

                    keyValueList = strAttr.split(':')
                    if len(keyValueList) > 1:
                        key = keyValueList[0]
                        value = keyValueList[1]

                        key = key.strip()
                        value = value.strip()

                        # Create new object of it
                        obj = {}
                        obj[key] = value

                        # Get list of properites and add the new element
                        listOfProperties = self.properties
                        listOfProperties.append(obj);
                        self.properties = listOfProperties


            return None
        elif os == 'windows':
            # Get Wifi Info using Windows
            if (printOutErrors):
                print ('Unsupported OS (Coming soon)')
            return None
        elif os == 'linux':
            # Get wifi info using Linux
            if (printOutErrors):
                print ('Unsupported OS (Coming soon)')
            return None
        else:
            if (printOutErrors):
                print ('Unsupported OS')
            return None

    def printProperties(self):
        for propertyObj in self.properties:
            # Get pairing
            if sys.version_info[0] < 3:
                # is python 3.x
                for key, value in propertyObj.items():
                    print ('["' + key + '" -> "' + value + '"]')
            else:
                # is python 2.x
                for key, value in propertyObj.iteritems():
                    print ('["' + key + '" -> "' + value + '"]')

    def get(self, propertyKey):
        for propertyObj in self.properties:
            if sys.version_info[0] < 3:
                for key, value in propertyObj.items():
                    if (key == propertyKey):
                        return value
            else:
                for key, value in propertyObj.iteritems():
                    if (key == propertyKey):
                        return value
