from ast import arg
import os
import argparse

try:
    from .sound_engine import SoundEngine
except ImportError:
    from c1c0_sounds.sound_engine import SoundEngine

cwd = os.getcwd()
default_folder = os.path.join(cwd, 'c1c0_sounds', 'chirp_parts')

parser = argparse.ArgumentParser(description='Convert morse code to audio.')
parser.add_argument('-f', '--folder', type=str, default=default_folder, help='Folder containing the audio files.')
parser.add_argument('-e', '--extension', type=str, default='.wav', help='Extension of the audio files.')
parser.add_argument('-m', '--morse', type=str, default='', help='Morse code to convert to audio.')
parser.add_argument('-t', '--text', type=str, default='', help='Text to convert to audio.')

args, unknown = parser.parse_known_args()

folder, extension, morse, text = args.folder, args.extension, args.morse, args.text

sound_engine = SoundEngine(folder=folder, ext=extension)
if text:
    sound_engine.play_text(text)
elif morse:
    sound_engine.play_morse(morse)
