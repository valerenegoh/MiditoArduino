# MiditoArduino
Stage 1 of SUTD Capstone 45 Pico Musical Engineering Installation project.<br/>
- Input: MIDI file, prefably downloaded from a sheet music site such as MuseScore.<br/>
- Output: Flashing LEDs timed to the music.<br/>

Part 1 of this project takes reference from [falcon](https://github.com/Tenchi2xh/Falcon/tree/master/falcon).
Part 2 requires connection to an Anrduino MEGA. The Arduino script requires you to set up an electronic circuit with 25 LEDs/solenoids/etc as shown in the video. Ensure they are wired to the corresponding pin numbers as in the `Arduino` file.

There are 4 ranges. The first three are common ranges provided by the Grand Illusions Music Boxes.<br/>
The fourth is a custom range of 25 notes created to provide better versatility.
1. 15-notes: C4-C6, non-chromatic 
2. 20-notes: C4-A6, non-chromatic
3. 30-notes: C0-E3, fully chromatic only in the middle
4. 25-notes: C4-C6, fully-chromatic

Add new MIDI files to `midi folder` and update them in `playlist.txt`

There are 2 parts to this project.

**Part 1: Preprocessing** transposes a MIDI file to fit X-note range. Outputs a txt document in `txt folder` that is readable by Arduino in Part 2.<br/>
1. Ensure python- midi is installed:<br/>
`pip install git+https://github.com/vishnubob/python-midi@feature/python3`
2. Edit the value of `sweetspot` in line 55/56 of `preprcessing.py`
3. Enter the following in your command line:<br/>
`python preprocessing.py [song] [range]`
For example, to play Do Re Mi in 25 note range:<br/>
`python preprocessing.py 2 GI25`

**Part 2: Running** reads the corresponding txt file and sends the notes to play to an Arduino via Serial communication. Result is the song being played in real time through e.g. LED flashing lights.<br/>
Connect to your Arduino and upload the sketch in `Arduino folder`.<br/>
Enter the following in your command line:<br/>
`python main.py`
