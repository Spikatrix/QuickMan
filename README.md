# QuickMan &nbsp; [![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/Spikatrix/QuickMan/blob/master/LICENSE)

Displays a subset of the `man` page output with information on the specified flags and options. Requires python3 to run.

## Example

	$ ./qm.py tar -vf -c --get
	NAME
	     tar — The GNU version of the tar archiving utility

	SYNOPSIS
	     tar [-] A --catenate --concatenate | c --create | d --diff --compare | --delete | r --append | t --list | --test-label | u --update | x --extract --get [options] [pathname ...]

	DESCRIPTION
	     Tar stores and extracts files from a tape or disk archive.

	SPECIFIED FLAGS AND OPTIONS
	     -v, --verbose
	            verbosely list files processed

	     -f, --file ARCHIVE
	            use archive file or device ARCHIVE

	     -c, --create
	            create a new archive

	     -x, --extract, --get
	            extract files from an archive
