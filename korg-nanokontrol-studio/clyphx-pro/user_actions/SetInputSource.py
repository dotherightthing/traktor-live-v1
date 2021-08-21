"""
Class: SetInputSource
Source: https://gist.github.com/dotherightthing/ece5b2baf955f7e969fc932d71fd753c
Package: Traktor TSI v2.3
_________________________________________________________________________________________

DESCRIPTION:

Sets Live's input channel to the selected Traktor deck

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
class SetInputSource(UserActionsBase):
    # Your class must implement this method.
    def create_actions(self):
        # called by on_selected_track_changed()
        self.add_clip_action('set_input_source', self.set_input_source)

    def on_selected_track_changed(self):
        empty_dict = {}
        self.set_input_source(empty_dict)

    def set_input_source(self, action_def):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        song_view = live_set.view
        tracks = list(live_set.tracks)
        selected_track = song_view.selected_track
        selected_track_index = list(tracks).index(selected_track)
        input = selected_track_index + 1
        action_list = ''

        if input < 5:
            for track_index in [5, 6, 7, 8]:
                action_list += str(track_index) + '/IN "' + str(input) + '"; '

            # self.canonical_parent.log_message(action_list)
            self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)