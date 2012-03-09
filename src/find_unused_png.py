#! python

import os
import fnmatch
import itertools
import re
import subprocess

def findFiles(pattern):
    for root, dirnames, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, pattern):
            filepath = os.path.join(root, filename)
            yield filepath;

def scanForPattern(pattern, files):
    for sourceFile in sourceFiles:
        fileHandle = open(sourceFile)
        fileContent = fileHandle.read()
        if fileContent.find(pattern) != -1:
            return True
    return False


if __name__ == "__main__":
    sourceFiles = [file for file in itertools.chain(
        findFiles("*.h"),
        findFiles("*.m"),
        findFiles("*.xib"),
        findFiles("*.plist"))];

    for image in findFiles("*.png"):
        imageFileName = image.split(os.sep)[-1]
        m = re.match("(.*?)(?:@2x|~iphone|~ipad)*\.png", imageFileName)
        pattern = m.group(1)
        if not scanForPattern(pattern, sourceFiles):
            print "%s" % image
            # For use with svn:
            #if re.search("@", image):
            #    image += "@"
            #subprocess.call(["svn", "rm", image])


