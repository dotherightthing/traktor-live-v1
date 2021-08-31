"""
Class: SelectedTrackLedStates
Source: https://gist.github.com/dotherightthing/ece5b2baf955f7e969fc932d71fd753c
Package: Traktor TSI v3.0
_________________________________________________________________________________________

PROBLEM:

A button / MIDI message can be used for EITHER X-Controls OR Button Bindings OR G-Controls.
See v.1.2.0 manual.
See https://forum.nativekontrol.com/thread/3906/beta-controls-accessory-clyphx-pro.

Button Bindings automatically handle LED feedback, but can't be used to trigger actions.
TRACK_SELECT_1 = CC, 1, 46, 0, 127, 1/SEL

X-Controls can trigger actions, LED can be lit by setting the CC value to 127, but implementation is rough.
For example, use of wait is required to reinstate the lit LED after the button which sets the state is released.
X_TRACK_SELECT_1 = CC, 1, 46, 0, 127, 1/sel ; update_select_leds MIDI CC 1, 46, 47, 48, 49, 50, 51, 52, 53 ; loop_led

X-Clips can trigger actions like X-Controls, but are verbose and difficult to edit.

SOLUTION:

G-Controls.txt maps the eight 'Select' MIDI controls to CXP's track SEL actions, with reliable LED control
and actions that leverage the simplicity of CXP macros and variables

Additional selection functionality uses user_actions which can also access variables.
Alternatively on_selected_track_changed(self) can be used, but this obscures what is happening.

X-Controls.txt maps the 'Set' MIDI control to CXP's CLIP LOOP action.
(Specifying on and off actions prevents having to push the button twice for each state).
CLIP_LOOP = CC, 1, 55, 0, 127, SEL/CLIP LOOP ON : SEL/CLIP LOOP OFF

on_selected_track_changed(self) calls extra actions whenever a track is selected in Live.
loop_led() is called here to update the lit state of the 'Set' control's LED.

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
        # called by G-Controls.txt
        self.add_clip_action('deck_leds', self.deck_leds)

        # called by Macros.txt
        self.add_clip_action('loop_led', self.loop_led)

    # def on_selected_track_changed(self):
    #     empty_dict = {}
    #     self.my_action(empty_dict, 'my_str')

    # when a track is selected
    # highlight the loop ('set') button LED
    # if the track contains a playing clip which is looping
    # there is no Button Binding for this, so a user action is required
    def loop_led(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        song_view = live_set.view
        selected_track = song_view.selected_track
        selected_track_name = selected_track.name
        action_list = ''
        action_list_off = '%MIDI_NANOKONTROL% %MIDI_CC_LOOP% 0'
        action_list_on = '%MIDI_NANOKONTROL% %MIDI_CC_LOOP% 127'

        # see https://docs.cycling74.com/max8/vignettes/live_object_model > playing_slot_index
        clip_stop_slot_fired_in_session_view = -2

        # tracks 1-4 are Traktor
        # tracks 5-8 are Live
        if (selected_track_name != '1') and (selected_track_name != '4'):
            # track = action_def['track'] # not working
            tracks = list(live_set.tracks)
            selected_track_index = list(tracks).index(selected_track)
            track = list(tracks)[selected_track_index]

            if track.playing_slot_index > clip_stop_slot_fired_in_session_view:
                playing_slot = list(track.clip_slots)[track.playing_slot_index]
                playing_clip = playing_slot.clip

                if playing_clip and playing_clip.looping:
                    action_list += action_list_on
                else:
                    action_list += action_list_off
            else:
                action_list += action_list_off

        # self.canonical_parent.log_message('loop_led: ' + action_list)
        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

    def deck_leds(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        song_view = live_set.view
        selected_track = song_view.selected_track
        input_name = selected_track.input_routing_type.display_name
        action_list = ''

        # TODO: is it possible to use a variable + a conditional instead?
        if (input_name == '1FX'):
            action_list += '%MIDI_NANOKONTROL% %MIDI_CC_SELECT_1% 127;'
            action_list += '%MIDI_NANOKONTROL% %MIDI_CC_SELECT_2% 127'
        elif (input_name == '4FX'):
            action_list += '%MIDI_NANOKONTROL% %MIDI_CC_SELECT_3% 127;'
            action_list += '%MIDI_NANOKONTROL% %MIDI_CC_SELECT_4% 127'

        # self.canonical_parent.log_message(action_list)
        self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)