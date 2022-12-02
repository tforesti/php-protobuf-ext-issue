#!/usr/bin/python3

# Generate the composer.json file

import glob
import json

filesConfig = []
psr4Config = {}

composerConfig = {
    "name": "example.com/test",
    "type": "library",
    "require": {
        "ext-grpc": "*",
        "ext-protobuf": "*",
        "grpc/grpc": "*",
        "google/gax": "*",
        "google/protobuf": "*"
    },
    "autoload": {
        "files": filesConfig,
        "psr-4": psr4Config
    }
}

for file in sorted(glob.glob("build/*.php")):
    filesConfig.append(file)

for directory in sorted(glob.glob("build/*/")):
    namespace = directory.strip("/").replace("build/", "")
    psr4Config[f"{namespace}\\"] = directory

composerString = json.dumps(composerConfig, indent=4, sort_keys=True)

with open('composer.json', 'w') as writer:
    writer.write(composerString)