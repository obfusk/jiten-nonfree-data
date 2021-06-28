#!/usr/bin/python3
import jiten.pitch as P
pitch = P.parse_pitch("pitch/PITCH")
P.pitch2sqldb(pitch, "pitch.sqlite3")
