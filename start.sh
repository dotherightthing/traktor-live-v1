#!/bin/bash

# File: ./start.sh
#
# Note:
# chmod a+x = Change access permissions of this file, to 'e[x]ecutable' for '[a]ll users'
#
# Example:
# ---
# chmod a+x start.sh
# ---
#
# Usage, disabling stdout for command output
#
# Example:
# ---
# ./start.sh >/dev/null
# ---

# e: exit the script if any statement returns a non-true return value
# v: print shell input lines as they are read (including all comments!)
set -e

n 14.17.4

open "/Applications/Bome MIDI Translator Pro.app"
open "/Applications/Native Instruments/Traktor Pro 3/Traktor.app"
open "/Applications/Ableton Live 10 Standard.app"