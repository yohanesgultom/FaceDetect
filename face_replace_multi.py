import os
import sys
import face_replace as fr

# current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))

# get relative path from arg
casc_path = sys.argv[1]
replacement_path = sys.argv[2]
in_path = sys.argv[3]
out_path = sys.argv[4]

# iterate dirs and files
for f in os.listdir(in_path):
    path = os.path.join(in_path, f)
    # print if file
    if os.path.isfile(path):
        # print os.path.join(dir_path, path)
        print 'Processing ' + path + '..'
        fr.replaceFaces(path, replacement_path, casc_path, out_path)
