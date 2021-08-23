"""
Class: SelectFxForSelectedTrack
Package: Traktor TSI v3.0
_________________________________________________________________________________________

DESCRIPTION:

Select the FX rack on the appropriate channel (1 FX for channel 1, 3 FX for channel 3)

TESTING:

```sh
# note: the version string will change if Live auto-updates itself
tail -f '/Users/dan/Library/Preferences/Ableton/Live 10.1.41/Log.txt'
```

```py
self.canonical_parent.log_message('Hello world')
```

IMPORTANT!

This file is not symlinked to the installation folder.
Manually copy changes to:
'/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions'
_________________________________________________________________________________________

"""

# Import UserActionsBase to extend it.
from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# Your class must extend UserActionsBase.
class SelectFxForSelectedTrack(UserActionsBase):
    # Your class must implement this method.
    def create_actions(self):
        # called by X-Controls.txt
        self.add_clip_action('select_track_fx', self.select_track_fx)

    def select_track_fx(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        song_view = live_set.view
        selected_track = song_view.selected_track
        selected_track_name = selected_track.name
        fx = args

        if (selected_track_name == '1') or (selected_track_name == '3'):
            action_list = '"' + selected_track_name + ' FX' + '"/DEV(' + fx + ') SEL'

            self.canonical_parent.log_message(action_list)
            self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)