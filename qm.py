#!/usr/bin/env python3

import sys
from quickman import QuickMan

def main():
    qm = QuickMan()
    qm.parse_command(sys.argv[1:])

if __name__ == "__main__":
    main()

