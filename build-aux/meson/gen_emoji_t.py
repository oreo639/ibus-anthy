#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print('impropper usage of command\n')
    exit(1)

with open(sys.argv[1]) as emojif, open(sys.argv[2]) as eachf, open(sys.argv[3], 'w') as of:
    last_pos = 0
    for line in iter(emojif.readline, ''):
        if not line.startswith('#'):
            emojif.seek(last_pos)
            break
        last_pos = emojif.tell()

    for line in eachf:
        if line.startswith('#@EMOJI_EMOJI@'):
            rest_of_file = eachf.readlines()
            of.writelines(emojif.readlines())
            of.writelines(rest_of_file)
            break
        of.write(line)
