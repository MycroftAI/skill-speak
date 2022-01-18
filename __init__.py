# Copyright 2016 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


# TODO - Localization

class SpeakSkill(MycroftSkill):
    @intent_handler(IntentBuilder("").require("Speak").require("Words"))
    def speak_back(self, message):
        """
            Repeat the utterance back to the user.

            TODO: The method is very english centric and will need
                  localization.
        """
        # Remove everything up to the speak keyword and repeat that
        with self.activity():
            utterance = message.data.get('utterance')
            repeat = re.sub('^.*?' + message.data['Speak'], '', utterance)
            self.speak(repeat.strip(), wait=True)

    def stop(self):
        pass


def create_skill():
    return SpeakSkill()
