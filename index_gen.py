#!/usr/bin/env python3

import os

seperator = "  "

# Based on https://stackoverflow.com/a/16974952
# Thank you based Ajay && based zaooza

def walk_lexicographic(path='.'):
    '''
    Traverses a directory tree. Each level is traversed in lexicographical
    order, and when a subdirectory is encountered it will be yielded
    immediately before being descended into, recursively, and then traversal of
    the original directory is continued. Entries beginning with a dot are never
    yielded, nor descended into.
    '''

    entries = sorted(
        (entry for entry in os.scandir(path) if entry.name[0] != '.'),
        key=lambda e: e.name
    )
    for entry in entries:
        yield entry
        if entry.is_dir():
            yield from walk_lexicographic(entry.path)

def toc_lines(path='.'):
    '''
    Yield Markdown for a table of contents for the files rooted at ``path'',
    line by line.
    '''
    for entry in walk_lexicographic(path):
        if entry.is_dir():
            yield (entry.path.count('/') - 1) * seperator + "* " + entry.name
        elif entry.name not in ('README.md', 'index.md', 'index_gen.py'):
            link = entry.path
            prefix = (entry.path.count('/') - 1) * seperator + "* "
            stem = entry.name.split('.')[0]
            yield f'{prefix}[{stem}]({link})'

with open("index.md", "w") as index_file:
    for toc_line in toc_lines():
        print(toc_line, file=index_file)
