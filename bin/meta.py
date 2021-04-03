#!/usr/bin/env python3

# Script for generating clean metadata files for superdirt and friends.
# (c) 2021 Alex McLean and contributors. Distributed under the terms of 
# GPLv3, see LICENSE for details.

import argparse
import pathlib
import os,sys
import json
import itertools
import getpass

version = "clean-0.1"

meta_subpath = "_soundmeta"

exts = {'.mp3': 'sample',
        '.wav': 'sample',
        '.scd': 'supercollider'
}

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
        extension = os.path.splitext(path)[1].lower()
        if extension in exts.keys():
            return True
    return False

def makeMeta(shortname, defaultMeta, pack_folder, subfolder, write):
    subpath = os.path.join(pack_folder, subfolder)

    metapath = os.path.join(pack_folder, meta_subpath)
    if not os.path.exists(metapath):
        os.makedirs(metapath)

    metafile = os.path.join(metapath, shortname + ".json")
    
    sounds = [fn for fn in os.listdir(subpath) if isSound(os.path.join(subpath, fn))]
    sounds.sort()

    sound_types = set(map(lambda x: exts[os.path.splitext(x)[1].lower()], sounds))
    if len(sound_types) > 1:
        defaultMeta['sound_type'] = "mixed"
    else:
        defaultMeta['sound_type'] = sound_types.pop()
    
    defaultMeta['sounds'] = list(map(lambda x: {'filename': os.path.join(subfolder,x), 'shortname': os.path.splitext(x)[0], 'description': ''}, sounds))
    
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
    parser.add_argument('pack_folder', type=str)
    parser.add_argument('--quiet', default=False, action="store_true")
    parser.add_argument('--sample-subfolder', dest="subfolder", default="", type=str)
    parser.add_argument('--shortname', type=str,
                        help='Identifier for the sampleset. Used to name the metadata file and to reference the sampleset elsewhere. Defaults to the name of the containing folder.'
    )
    parser.add_argument('--maintainer', type=str,
                        help='Name of maintainer'
    )
    parser.add_argument('--email', type=str,
                        help='Email of maintainer'
    )
    parser.add_argument('--copyright', type=str,
                        help='Copyright statement, e.g. (c) Gregory Coleman, 1969'
    )
    parser.add_argument('--license', type=str,
                        help='e.g. CC0 for creative commons zero (public domain)'
    )
    parser.add_argument('--provenance', type=str,
                        help='Where the samples came from, e.g. a freesound.org URL'
    )
    parser.add_argument('--description', type=str,
                        help='Description of a sample pack'
    )
    parser.add_argument('--write', default=False,
                        help='write/re-write the metadata with default values', action="store_true"
    )

    args = parser.parse_args()
    if (not os.path.exists(args.pack_folder)):
        sys.exit("Couldn't open '" + args.pack_folder + "'")
        subpath = os.path.join(args.pack_folder, args.subfolder)
        if (not os.path.exists(subpath)):
            sys.exit("Couldn't open '" + subpath + "'")
    return args

args = getArgs()

pack_folder = args.pack_folder
if args.shortname:
    shortname = args.shortname
else:
    shortname = os.path.basename(os.path.normpath(os.path.join(args.pack_folder, args.subfolder)))

defaultMeta = {
    'metadata-format': version,
    'shortname': shortname,
    'license': args.license if args.license else "unknown",
    'copyright': args.copyright if args.copyright else "unknown",
    'provenance': args.provenance if args.provenance else "",
    'maintainer': args.maintainer if args.maintainer else getpass.getuser(),
    'email': args.email if args.email else "",
    'description': args.description if args.description else "",
}


meta = makeMeta(shortname, defaultMeta, pack_folder, args.subfolder, args.write)

if not args.quiet:
    print(json.dumps(meta, sort_keys=True, indent=2))

exit(0)
