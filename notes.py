#!/usr/bin/env python
# -*- coding: utf-8 -*-

import StringIO
import os

NOTE_PATH = os.environ.get('NOTES_PATH')

def list_tag(tags=[]):
    if len(tags) == 0:
        tags = os.listdir(NOTE_PATH)

    for tag in tags:
        tag = os.path.splitext(tag)[0]
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
    if not argv:
        print """usage: notes @myTag @tag2 \"my notes\" # Add new notes into @myTag and @tag2 
       notes @myTag                  # List notes into @myTag
       notes tags                    # List all tags
            """
        return

    tags = []
    buffer = StringIO.StringIO()
    started = False
    
    for arg in argv:
        if arg == "tags":
            list_tag()
            break
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

