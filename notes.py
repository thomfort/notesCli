#!/usr/bin/env python
# -*- coding: utf-8 -*-

import StringIO
import os

NOTE_PATH = os.environ.get('NOTES_PATH')

def list_tag(tags):
    if len(tags) == 0:
        pass
    for tag in tags:    
        filename = NOTE_PATH + "/" + tag + ".txt"
        if not os.path.isfile(filename):            
            continue
        f = open(filename)
        if os.stat(filename).st_size == 0:
            continue
        print "@"+tag
        print f.read()
        f.close()  

def add_note(*argv):
    tags = []
    buffer = StringIO.StringIO()
    started = False
    for arg in argv:
        if arg[0] == "@":
            tags.append(arg[1:])
            if started is False:
                continue
        buffer.write(" " + arg)
        started = True    

    message = buffer.getvalue()
    
    if not message:
        list_tag(tags)
        return

    print tags
    print message
    message = "* " + message

    for tag in tags:
        fileName = NOTE_PATH + "/" + tag + ".txt"
        f = open(fileName, 'a+')
        f.write(message + "\n\r")
        f.close()

    buffer.close()

if __name__ == "__main__":
    import sys
    add_note(*sys.argv[1:])

