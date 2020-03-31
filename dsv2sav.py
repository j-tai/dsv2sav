#!/usr/bin/env python3
import sys


def usage():
    """Print usage information to stderr and exit."""
    print("""\
Usage: dsv2sav.py INPUT OUTPUT

Convert DSV (DeSmuME save file) to SAV/SRM (raw save file) and vice versa.

INPUT and OUTPUT must have appropriate file extensions.

If OUTPUT is a DSV file, then it must already exist and contain DSV data from
the correct NDS game. Its contents will be overwritten with the data from the
SAV/SRM file.
""", file=sys.stderr)
    exit(2)


def get_extension(filename):
    """Get the file extension of the given filename."""
    if '.' not in filename:
        return None
    return filename.split('.')[-1]


DSV_FOOTER = b'|<--Snip above here to create a raw sav by excluding this DeSmuME savedata footer:'
DSV_COOKIE = b'|-DESMUME SAVE-|'
DSV_FOOTER_LEN = len(DSV_FOOTER) + 24 + len(DSV_COOKIE)


def dsv_to_sav(dsv_file, sav_file):
    # Just trim off the DeSmuME footer
    with open(dsv_file, 'rb') as dsv, open(sav_file, 'wb') as sav:
        dsv_data = dsv.read()
        dsv_footer = dsv_data[-DSV_FOOTER_LEN:]
        if not dsv_footer.endswith(DSV_COOKIE):
            raise ValueError('Invalid DSV data (cookie mismatch)')
        sav_data = dsv_data[:-DSV_FOOTER_LEN]
        sav.write(sav_data)


def sav_to_dsv(sav_file, dsv_file):
    with open(sav_file, 'rb') as sav, open(dsv_file, 'r+b') as dsv:
        sav_data = sav.read()
        dsv.seek(-DSV_FOOTER_LEN, 2)
        dsv_footer = dsv.read()
        if not dsv_footer.endswith(DSV_COOKIE):
            raise ValueError('Invalid DSV data (cookie mismatch)')
        if dsv.tell() != len(sav_data) + DSV_FOOTER_LEN:
            raise ValueError('Invalid DSV data (data length mismatch)')
        dsv.seek(0)
        dsv.write(sav_data)


VALID_EXTENSIONS = ('dsv', 'sav', 'srm')

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        usage()
    in_file, out_file = args
    in_ext, out_ext = map(get_extension, args)
    if in_ext not in VALID_EXTENSIONS or out_ext not in VALID_EXTENSIONS:
        usage()
    if (in_ext == 'dsv') == (out_ext == 'dsv'):
        # Input and output cannot be the same type
        usage()
    if in_ext == 'dsv':
        dsv_to_sav(in_file, out_file)
    else:
        sav_to_dsv(in_file, out_file)


if __name__ == '__main__':
    main()
