# pip install torch transformers diffusers transformers accelerate matplotlib librosa --break-system-packages
# pip install IPython --break-system-packages

# from transformers import pipeline
# from IPython.display import Audio

# pipe = pipeline('text-to-speech') # suno

# output = pipe("Hello, how are you today")
# audio=Audio(data=output['audio'], rate=output['sampling_rate'])


from transformers import pipeline
from IPython.display import Audio
import numpy as np
from scipy.io import wavfile

pipe = pipeline("text-to-speech")  # or specify your model

out = pipe("Hello, how are you today")

audio = out["audio"]          # typically float32, shape (T,) or (1, T)
sr = out["sampling_rate"]

# Remove batch dimension if present: (1, T) -> (T,)
if audio.ndim > 1:
    audio = audio[0]

# Ensure 1‑D or (T, 1) shape
audio = np.asarray(audio).astype(np.float32)

# Option 1: write as float WAV (supported in recent SciPy)
wavfile.write("output/audio.wav", sr, audio)