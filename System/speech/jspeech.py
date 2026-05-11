# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

'''
   The followinig script is written for the Cortex archive


   -> I am trying to make Cortex speak now beacuse by the end of this year i want my ai to be able to speech for himself and estimate data more easily

'''

import speech_recognition as speech

src = speech.Recognizer()
with speech.Microphone() as source:
    audio = src.listen(source)
    print(src.recognize_google(audio))
