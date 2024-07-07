"""This module processes midi file data to train a neural network."""

import os
import numpy as np
from music21 import converter, instrument, note, chord

def get_notes(midi_class):
    """Gather notes and chords from all midi files from a specific class."""

    notes = []

    for file in os.walk('bach-midi/'):
    

if __name__ == '__main__':
    print('testing stuff...')