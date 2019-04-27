# -*- encoding: utf-8 -*-

from sys import argv

import midi

from util import *
from boxes import *

# basename = "Stand_by_me"
# box = GI15    # change to GI15, GI20, GI30 or GI25


def main(argv):
    basename = argv[0]
    box = eval(argv[1])
    
    midi_file = "midi/%s.mid" % basename
    print("Reading MIDI file: %s" % basename)
    tracks = midi.read_midifile(midi_file)
    print("Found %d tracks:" % len(tracks))

    all_notes_on = []
    all_notes_off = []
    for i, track in enumerate(tracks):
        notes_on = list(filter(lambda note: note.is_event(midi.events.NoteOnEvent.statusmsg), track))
        notes_off = list(filter(lambda note: note.is_event(midi.events.NoteOffEvent.statusmsg), track))
        print("- Track #%d: %d notes"  % (i, len(list(notes_on))))
        all_notes_on.extend(notes_on)
        all_notes_off.extend(notes_off)
        
    print("Total of %d notes" % len(all_notes_on))
    print("Song is %d beats long" % beats(tracks))

    all_distances = []

    for key in range(-48, 49):
        pitches = list(map(lambda note: note.pitch + key, all_notes_on))
        distances = map(box.distance, pitches)
        
        try:
            average_distance = sum(distances) / len(pitches)
        except ZeroDivisionError:
            average_distance = 0
            print("Error! Zero Division Error!")
        all_distances.append((average_distance, key))
    
    print("Size of all_distances: %d" % len(all_distances))
    best_distance, transpose = min(all_distances, key=lambda t: t[0])

    print("Best distance %f with transpose key %d, transposing" % (best_distance, transpose))

    for note in all_notes_on:
        closest = box.closest(note.pitch + transpose)
        note.set_pitch(closest)
        
    # write to file
    notes_perbeat = dict((beat,[]) for beat in range(beats(tracks)*2))
    
    for i in range(len(tracks)):
#        if i == 1:    # uncomment this if you want to only output melody/accompaniment
            start = 0
            notes_on = list(filter(lambda note: note.is_event(midi.events.NoteOnEvent.statusmsg), tracks[i]))
            for note in notes_on:
                start += int(2*((note.tick + 1)/tracks.resolution))
#                print(note, start)
                if note.velocity > 0:
                    notes_perbeat[start].append(note.pitch)
    
    file = open("txt/%s_%s.txt" % (basename, box.symbol), "w")
    for notes_list in notes_perbeat.values():
#        print(notes_list)
        file.write(" ".join(str(note) for note in notes_list) + "\n")

#    midi.write_midifile("midi/%s_%s.mid" % (basename, box.symbol), tracks)

#    punch(basename, tracks, box)

    
if __name__ == '__main__':
    main(argv[1:])
    