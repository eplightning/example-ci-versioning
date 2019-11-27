#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import git.repo
from packaging.version import Version

def parse_args():
    parser = argparse.ArgumentParser(description='Calculate next version of application based on git tags')
    parser.add_argument('-f', '--repository-path', default='.', help='Repository path')
    return parser.parse_args()

def get_valid_versions(repo):
    def parse_tag(t):
        try:
            version = Version(t.name)
        except:
            return None
        else:
            return version

    return filter(lambda x: x != None, map(parse_tag, repo.tags))

def transform_to_next_semver(version):
    release = version.release

    if len(release) >= 3:
        fragments = [release[0], release[1], release[2] + 1]
    elif len(release) == 2:
        fragments = [release[0], release[1], 0]
    else:
        fragments = [release[0], 0, 0]

    return '.'.join([str(x) for x in fragments])

if __name__  == '__main__':
    args = parse_args()
    repo = git.repo.Repo(args.repository_path)
    versions = sorted(get_valid_versions(repo))
    last_version = versions[-1]

    print(transform_to_next_semver(last_version))
