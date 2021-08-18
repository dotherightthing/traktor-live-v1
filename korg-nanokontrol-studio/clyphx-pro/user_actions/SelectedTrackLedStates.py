"""
Class: SelectedTrackLedStates
Source: https://gist.github.com/dotherightthing/ece5b2baf955f7e969fc932d71fd753c
Package: Traktor TSI v2.3
_________________________________________________________________________________________

PROBLEM:

A button / MIDI message can be used for EITHER X-Controls OR Button Bindings OR G-Controls.
See v.1.2.0 manual.
See https://forum.nativekontrol.com/thread/3906/beta-controls-accessory-clyphx-pro.

Button Bindings automatically handle LED feedback, but can't be used to trigger actions.
TRACK_SELECT_1 = CC, 1, 46, 0, 127, 1/SEL

X-Controls can trigger actions, LED can be lit by setting the CC value to 127, but implementation is rough.
For example, use of wait is required to reinstate the lit LED after the button which sets the state is released.
X_TRACK_SELECT_1 = CC, 1, 46, 0, 127, 1/sel ; update_select_leds MIDI CC 1, 46, 47, 48, 49, 50, 51, 52, 53 ; update_loop_led MIDI CC 1 55

X-Clips can trigger actions like X-Controls, but are verbose and difficult to edit.

SOLUTION:

Button Bindings.txt maps the eight 'Select' MIDI controls to CXP's track SEL actions. This provides the best LED control.
TRACK_1_SELECT = CC, 1, 46, 0, 127, 1/SEL
TRACK_2_SELECT = CC, 1, 47, 0, 127, 2/SEL
TRACK_3_SELECT = CC, 1, 48, 0, 127, 3/SEL
TRACK_4_SELECT = CC, 1, 49, 0, 127, 4/SEL
TRACK_5_SELECT = CC, 1, 50, 0, 127, 5/SEL
TRACK_6_SELECT = CC, 1, 51, 0, 127, 6/SEL
TRACK_7_SELECT = CC, 1, 52, 0, 127, 7/SEL
TRACK_8_SELECT = CC, 1, 53, 0, 127, 8/SEL

X-Controls.txt maps the 'Set' MIDI control to CXP's CLIP LOOP action.
(Specifying on and off actions prevents having to push the button twice for each state).
CLIP_LOOP = CC, 1, 55, 0, 127, SEL/CLIP LOOP ON : SEL/CLIP LOOP OFF

on_selected_track_changed(self) calls extra actions whenever a track is selected in Live.
update_loop_led() is called here to update the lit state of the 'Set' control's LED.

KORG KONTROL Editor sets the corresponding Button Behaviors (for nanoKONTROL Studio):
* 'clip loop' button/indicator = 'Set' button = Button Behavior = Toggle
* 'track select' button/indicator = 'Select' buttons = Button Behavior = Momentary

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
class SelectedTrackLedStates(UserActionsBase):
    # Your class must implement this method.
    def create_actions(self):
        # this action is only called via on_selected_track_changed()
        self.add_track_action('update_loop_led', self.update_loop_led)

    def on_selected_track_changed(self):
        empty_dict = {}
        self.update_loop_led(empty_dict, 'MIDI CC 1 55')

    # when a track is selected
    # highlight the loop ('set') button LED
    # if the track contains a playing clip which is looping
    # there is no Button Binding for this, so a user action is required
    def update_loop_led(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        cc = args

        # Not used, as fired from an X-Clip which selects a different track
        # track_object = action_def['track']
        # track_index = list(live_set.tracks).index(track_object)

        song_view = live_set.view
        tracks = list(live_set.tracks)
        selected_track = song_view.selected_track
        selected_track_index = list(tracks).index(selected_track)
        track = list(tracks)[selected_track_index]

        action_list = ''
        action_list_off = cc + ' 0' # MIDI CC X Y 0
        action_list_on = cc + ' 127' # MIDI CC X Y 127

        # see https://docs.cycling74.com/max8/vignettes/live_object_model > playing_slot_index
        clip_stop_slot_fired_in_session_view = -2

        if track.playing_slot_index > clip_stop_slot_fired_in_session_view:
            playing_slot = list(track.clip_slots)[track.playing_slot_index]
            playing_clip = playing_slot.clip

            if playing_clip and playing_clip.looping:
                action_list += action_list_on
            else:
                action_list += action_list_off

        # self.canonical_parent.log_message('update_loop_led: ' + action_list)
        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)