import time
import fluidsynth

fs = fluidsynth.Synth(gain=0.8)
fs.start()

sfid = fs.sfload("Yamaha_C3_Grand_Piano.sf2")
fs.program_select(0, sfid, 0, 0)

# fs.noteon(0, 60, 30)
# fs.noteon(0, 64, 30)
# fs.noteon(0, 67, 30)
# fs.noteon(0, 72, 30)

fs.noteon(0, 21, 30)

time.sleep(1.0)

# fs.noteoff(0, 60)
# fs.noteoff(0, 64)
# fs.noteoff(0, 67)
# fs.noteoff(0, 72)

fs.noteoff(0, 1)

time.sleep(1.0)

fs.delete()
