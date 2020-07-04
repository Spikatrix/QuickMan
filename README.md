# QuickMan &nbsp; [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

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
