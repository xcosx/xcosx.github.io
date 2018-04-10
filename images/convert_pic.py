#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
from subprocess import call
import shlex
# import glob

if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    optp.add_option("-f", "--file", dest="file",
                    help="JID to use")

    opts, args = optp.parse_args()

    if opts.file is None:
        opts.file = raw_input("Datei: ")

    print('Konvertiere die Datei: ' + str(opts.file))
    # call("clear")
    klassischer_befehl = "convert " + str(file) + " -resize 900x300 -gravity center -background transparent -extent 900x300 /home/effe/Git/xcosx.github.io/content/images/tuete3.png"
    print(klassischer_befehl)
    befehl_fuer_call = shlex.split(klassischer_befehl)
    call(befehl_fuer_call)
