#!/usr/bin/env python3
"""Checks that this repository is a Strix theme repository, layout 1. Strix runs the same rules before it
takes a connected repository; CI runs this file on every push.

    python3 check.py

Only the Python standard library. The colours are checked by the theme engine itself (see the workflow).
"""
import os, re, struct, sys, tomllib

ROOT = os.path.dirname(os.path.abspath(__file__))
BUILT_IN = {'saturnus', 'janus', 'apollo', 'mars', 'vulcanus', 'neptunus', 'pluto', 'bacchus', 'neutral'}
ID = re.compile(r'[a-z][a-z0-9]*(-[a-z0-9]+)*')
THEME_FILES = {'theme.toml', 'wallpaper.jpg', 'wallpaper.toml'}
LICENCES = {'public domain', 'CC0'}
MAX_WALLPAPER = 4 * 1024 * 1024


def jpeg_size(path):
    """Width and height from the first frame header, or None when the file is no JPEG."""
    with open(path, 'rb') as f:
        if f.read(2) != b'\xff\xd8':
            return None
        while True:
            b = f.read(1)
            while b == b'\xff':
                b = f.read(1)
            if not b:
                return None
            marker = b[0]
            if marker in (0xd8, 0x01) or 0xd0 <= marker <= 0xd7:
                continue
            length = struct.unpack('>H', f.read(2))[0]
            if 0xc0 <= marker <= 0xcf and marker not in (0xc4, 0xc8, 0xcc):
                h, w = struct.unpack('>xHH', f.read(5))
                return w, h
            f.seek(length - 2, 1)


def main():
    fails = []
    marker = os.path.join(ROOT, 'strix-themes.toml')
    if not os.path.isfile(marker):
        print('FAIL strix-themes.toml is missing: without it Strix does not take the repository')
        return 1
    meta = tomllib.load(open(marker, 'rb'))
    if meta.get('layout') != 1:
        fails.append('strix-themes.toml: layout must be 1')
    for key in ('name', 'description'):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            fails.append('strix-themes.toml: %s is missing' % key)
    tdir = os.path.join(ROOT, 'themes')
    ids = sorted(d for d in os.listdir(tdir) if os.path.isdir(os.path.join(tdir, d))) if os.path.isdir(tdir) else []
    for f in (os.listdir(tdir) if os.path.isdir(tdir) else []):
        if not os.path.isdir(os.path.join(tdir, f)) and f != '.gitkeep':
            fails.append('themes/%s: only folders belong in themes/' % f)
    for i in ids:
        where = 'themes/%s' % i
        if not ID.fullmatch(i) or len(i) > 32:
            fails.append('%s: the id must be lowercase letters, digits and single hyphens, at most 32 characters' % where)
        if i in BUILT_IN:
            fails.append('%s: %s is a theme of Strix itself; pick another id' % (where, i))
        files = set(os.listdir(os.path.join(tdir, i)))
        for missing in sorted(THEME_FILES - files):
            fails.append('%s: %s is missing' % (where, missing))
        for extra in sorted(files - THEME_FILES):
            fails.append('%s: %s does not belong here; a theme holds only %s' % (where, extra, ', '.join(sorted(THEME_FILES))))
        wp = os.path.join(tdir, i, 'wallpaper.jpg')
        if os.path.isfile(wp):
            if jpeg_size(wp) != (2560, 1440):
                fails.append('%s: wallpaper.jpg must be a JPEG of 2560 by 1440' % where)
            if os.path.getsize(wp) > MAX_WALLPAPER:
                fails.append('%s: wallpaper.jpg is larger than 4 MiB' % where)
        wt = os.path.join(tdir, i, 'wallpaper.toml')
        if os.path.isfile(wt):
            w = tomllib.load(open(wt, 'rb'))
            for key in ('caption', 'credit'):
                if not isinstance(w.get(key), str) or not w[key].strip():
                    fails.append('%s/wallpaper.toml: %s is missing' % (where, key))
            if w.get('licence') not in LICENCES:
                fails.append('%s/wallpaper.toml: licence must be "public domain" or "CC0"' % where)
            unknown = set(w) - {'caption', 'credit', 'licence'}
            if unknown:
                fails.append('%s/wallpaper.toml: unknown keys %s' % (where, ', '.join(sorted(unknown))))
    for f in fails:
        print('FAIL ' + f)
    print('%d theme%s, FAILS %d' % (len(ids), '' if len(ids) == 1 else 's', len(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
