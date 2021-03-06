#    "chases": {
#        "chaseName1": [
#            #{ "cueList": {cue1, cue2, cue3}, "duration": time_in_seconds, "nextAction":Continue|Stop|Loop, "initialTransitionDuration": time_in_seconds},
#            { "cueList": {"cueName2", "cueName3"}, "duration": 10.5, "nextAction":"Continue", "initialTransitionDuration": 2},
#            { "cueList": {"cueName1"}, "duration": 5, "nextAction":"Continue", "initialTransitionDuration": 1},
#            { "cueList": {"cueName3"}, "duration": 30, "nextAction":"Loop", "initialTransitionDuration": 0}
#        ],
#        "chaseName2": [
#            { "cueList": {"cueName2", "cueName3"}, "duration": 10.5, "nextAction":"Continue", "initialTransitionDuration": 0},
#            { "cueList": {"cueName1"}, "duration": 5, "nextAction":"Continue", "initialTransitionDuration": 2},
#            { "cueList": {"cueName3"}, "duration": 30, "nextAction":"Stop", "initialTransitionDuration": 5}
#        ]
#    },

import time,  logging
from artnet import dmx_frame, dmx_fixture, dmx_effects, dmx_rig,  dmx_cue

from artnet import shared
#logging.basicConfig(format='%(levelname)s:%(message)s', filename='artNet_controller.log', level=logging.DEBUG)
#log = logging.getLogger(__name__)


class Chase():
    def __init__(self, chaseName,  chase):
        self.chaseName = chaseName
        self.chase = chase
     

    def getFrame(self):
        theFrame = dmx_frame.Frame()
# A FINALISER 

        # Set the values of the fixture
        for fixtureName, parameter in self.cueFixtureList.items():
            shared.log.debug("Cue: %s Fixture: %s" % (self.name, fixtureName))
            for actionCommand, actionValue in parameter.items():
                shared.log.debug(" - action: %s - %s" % (actionCommand, actionValue))
                fixtureName.actionCommand(actionValue)
            
            # Merge this values in the current frame
            theFrame.merge(fixtureName.getFrame())
            
        # Set the values of the group
        for groupName, parameter in self.cueGroupList.items():
            shared.log.debug("Cue: %s Group: %s" % (self.name, groupName))
            for actionCommand, actionValue in parameter.items():
                shared.log.debug(" - action: %s - %s" % (actionCommand, actionValue))
                groupName.actionCommand(actionValue)

            # Merge this values in the current frame
            theFrame.merge(groupName.getFrame())

        # Set the values of the effect

        return theFrame

