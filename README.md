# dsv2sav

A command-line utility to convert between DSV (DeSmuME save file) and SAV/SRM formats.

## Usage

```
Usage: dsv2sav.py INPUT OUTPUT

Convert DSV (DeSmuME save file) to SAV/SRM (raw save file) and vice versa.

INPUT and OUTPUT must have appropriate file extensions.

If OUTPUT is a DSV file, then it must already exist and contain DSV data from
the correct NDS game. Its contents will be overwritten with the data from the
SAV/SRM file.
```

### Convert a SAV or SRM file to DSV file

First, run the NDS game whose save data you want to convert in DeSmuME to create an empty DSV file. Then, you can copy the SAV/SRM into the DSV file:

```console
$ ./dsv2sav.py /path/to/input.sav /path/to/output.dsv
```

### Convert a DSV file to a SAV or SRM file

You do not need a blank SAV or SRM file for this.

```console
$ ./dsv2sav.py /path/to/input.dsv /path/to/output.sav
```

### Convert between SAV and SRM files

SAV and SRM files are the same file format. Simply rename the file and change its extension.

## License

[MIT License](LICENSE).
