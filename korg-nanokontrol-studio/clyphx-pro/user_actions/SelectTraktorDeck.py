"""
Class: SelectTraktorDeck
Package: Traktor TSI v3.0
_________________________________________________________________________________________

DESCRIPTION:

Fires a MIDI CC to select the sampler source deck in Traktor

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
class SelectTraktorDeck(UserActionsBase):
    # Your class must implement this method.
    def create_actions(self):
        # called by X-Controls.txt
        self.add_clip_action('select_traktor_deck_a_during_recording', self.select_traktor_deck_a_during_recording)
        self.add_clip_action('select_traktor_deck_b_during_recording', self.select_traktor_deck_b_during_recording)
        self.add_clip_action('select_traktor_deck_d_after_recording', self.select_traktor_deck_d_after_recording)

    # select sampler source track during recording
    def select_traktor_deck_a_during_recording(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()
        song_view = live_set.view
        selected_track = song_view.selected_track
        input_name = selected_track.input_routing_type.display_name
        action_list = args

        if input_name == '1FX':
            self.canonical_parent.log_message(action_list)
            self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

    # select sampler source track during recording
    def select_traktor_deck_b_during_recording(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()
        song_view = live_set.view
        selected_track = song_view.selected_track
        input_name = selected_track.input_routing_type.display_name
        action_list = args

        if input_name == '4FX':
            self.canonical_parent.log_message(action_list)
            self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

    # select dummy track after recording
    def select_traktor_deck_d_after_recording(self, action_def, args):
        action_list = args

        self.canonical_parent.log_message(action_list)
        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)