#!/usr/bin/env python3

import argparse
import pathlib
import os,sys
import json
import itertools

def merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        d = dict(a)
        d.update({k: merge(a.get(k, None), b[k]) for k in b})
        return d

    if isinstance(a, list) and isinstance(b, list):
        return [merge(x, y) for x, y in itertools.zip_longest(a, b)]

    return a if b is None else b


def isSound(path):
    if os.path.isfile(path):
        extension = os.path.splitext(path)[1]
        if extension in ['.wav','.mp3']:
            return True
    return False

def readMeta(pack_folder, subpath, write):
    metafile = os.path.join(pack_folder, "clean-metadata.json")
    sounds = [fn for fn in os.listdir(subpath) if isSound(os.path.join(subpath, fn))]
    s = list(map(lambda x: {'filename': x, 'type': 'sample'}, sounds))
    defaultMeta = {
        'name': os.path.basename(os.path.normpath(pack_folder)),
        'sounds': s
    }
     
    if (os.path.exists(metafile)):
        with open(metafile) as json_file:
            meta = json.load(json_file)
            meta = merge(defaultMeta,meta)
    else:
        meta = defaultMeta
        
    if write:
        with open(metafile, 'w') as json_file:
            json.dump(meta, json_file, sort_keys=True, indent=2)

    return(meta)

    
def getArgs():
    parser = argparse.ArgumentParser(description='Create metadata for a sample folder.')
    parser.add_argument('pack_folder', nargs='+', type=str)
    parser.add_argument('--sample-subfolder', dest="subfolder", default="sounds", type=str)
    parser.add_argument('--write', default=False,
                        help='write/re-write the metadata with default values', action="store_true"
    )

    args = parser.parse_args()
    for pack_folder in args.pack_folder:
        if (not os.path.exists(pack_folder)):
            sys.exit("Couldn't open '" + pack_folder + "'")
            subpath = os.path.join(pack_folder, args.subfolder)
            if (not os.path.exists(subpath)):
                sys.exit("Couldn't open '" + subpath + "'")
    return args

args = getArgs()

for pack_folder in args.pack_folder:
    subpath = os.path.join(pack_folder, args.subfolder)
    meta = readMeta(pack_folder, subpath, args.write)

exit(0)
