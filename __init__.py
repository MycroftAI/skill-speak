# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

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
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['Speak'], '', utterance)
        self.speak(repeat.strip())

    def stop(self):
        pass


def create_skill():
    return SpeakSkill()
