#!/usr/bin/env python3
import argparse
import tempfile
from pathlib import Path
import sounddevice as sd
import soundfile as sf
from openai import OpenAI
import os, sys

# Set command-line arguments
parser = argparse.ArgumentParser(description="AI Speech Generator")
parser.add_argument("input", nargs='*', default="", help="Direct input text for speech synthesis")
parser.add_argument("-v", "--voice", default="onyx", help="Voice model to use (default: onyx)")
parser.add_argument("-f", "--file", help="Text file to read input from")
parser.add_argument("-o", "--output", help="Output file path for the generated speech")
parser.add_argument("-r", "--rate", type=float, default=1.0, help="Playback speed of the generated speech (0.25 to 4.0)")

# Parse command-line arguments
args = parser.parse_args()

# If no arguments were provided, show help information and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Read file content as input if a file parameter is specified
if args.file:
    with open(args.file, 'r') as file:
        args.input = file.read()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])  # api_key = "sk-...."

# Set the output file path
if args.output:
    speech_file_path = Path(args.output)
else:
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3', dir='/tmp')
    speech_file_path = Path(temp_file.name)

if args.input:
    args.input = ' '.join(args.input)
# Generate audio
response = client.audio.speech.create(
    model="tts-1",
    voice=args.voice,
    input=args.input,
    speed=args.rate,
)

# Save audio stream to file
response.stream_to_file(str(speech_file_path))

# Read the audio file
audio_data, sample_rate = sf.read(str(speech_file_path))

audio_data, sample_rate = sf.read(speech_file_path)
sd.play(audio_data, sample_rate)
sd.wait()
