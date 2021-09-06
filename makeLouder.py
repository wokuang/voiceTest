from pydub import AudioSegment
from pydub.playback import play

file_name = '/Users/bruce_t_wang/dev/voiceTest/sutra_earth04.mp3'
song = AudioSegment.from_mp3(file_name)

# boost volume by 6dB
louder_song = song + 6

# reduce volume by 3dB
#quieter_song = song - 3

#Play song
#play(louder_song)

#save louder song 
louder_song.export("louder_song.mp3", format='mp3')
