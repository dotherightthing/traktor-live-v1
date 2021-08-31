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
        self.add_clip_action('select_traktor_deck', self.select_traktor_deck)
        self.add_clip_action('deselect_traktor_deck', self.deselect_traktor_deck)

    # select sampler source track during recording
    def select_traktor_deck(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()
        song_view = live_set.view
        selected_track = song_view.selected_track
        input_name = selected_track.input_routing_type.display_name
        action_list = ''

        if input_name == '1FX':
            action_list += 'MIDIB %MIDI_CC_TRAKTOR_DECK_A% 127'
        elif input_name == '4FX':
            action_list += 'MIDIB %MIDI_CC_TRAKTOR_DECK_B% 127'

        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

    # select dummy track after recording
    def deselect_traktor_deck(self, action_def, args):
        action_list = 'MIDIB %MIDI_CC_TRAKTOR_DECK_D% 127'

        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)