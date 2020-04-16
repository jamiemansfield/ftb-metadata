import json
import os
from os import walk

changelogs = []
for (dirpath, dirnames, filenames) in walk("changelogs"):
    changelogs.extend(filenames)
    break

for changelog in changelogs:
    packSlug = changelog[0:changelog.find('_')]
    versionSlug = changelog[changelog.find('_') + 1:-4]
    print(packSlug + " " + versionSlug)

    cl = {}
    if os.path.isfile("pack/" + packSlug + ".json"):
        with open("pack/" + packSlug + ".json") as changelogR:
            cl = json.load(changelogR)

    try:
        overrides = cl["changelogs"]
    except KeyError:
        overrides = {}

    with open("changelogs/" + changelog) as rawCl:
        overrides[versionSlug] = rawCl.read()

    cl["changelogs"] = overrides

    with open("pack/" + packSlug + ".json", "w+") as changelogW:
        json.dump(cl, changelogW, indent=4)
        changelogW.write("\n")
