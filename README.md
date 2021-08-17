# traktor-template-nk

Traktor template for KORG nanoKONTROL + nanoKEY Studio.

Includes a four channel sampler using Ableton Live.

This is a private project, documented here for my own benefit and shared in case any part proves useful.

---

## Purpose

The purpose of this setup is to replace Traktor’s Loop Recorder and Remix Decks with Ableton Live.

### Replace Traktor’s Remix Decks

Traktor’s Remix Decks mostly work fine when resampling directly from a deck.

However when keylock pitching is used, the recorded pitch often does not match the source deck.

### Replace Traktor’s Loop Recorder

To capture global FX like reverb and gating, Traktor’s Loop Recorder must be used.

The Loop Recorder is problematic because it records loops slightly too long. Samples glitch on repeat and drift out of time with the source material.

---

## Components

1. **Sound Card:** External Headphones (headphones or Minirig plugged into headphone jack)
2. **Virtual Sound Card:** Rogue Amoeba Loopback (v2)
3. **DJ Application + MIDI Clock:** Traktor (v3.4.2)
4. **Sampler & Sequencer:** Ableton Live (v10) + ClyphX Pro (v1.2.0)
5. **Controller Mapping:** nanoKONTROL Studio + nanoKEY Studio + Traktor (v3.4.2) + KORG KONTROL Editor (+ Ableton Live (v10) + ClyphX Pro (v1.2.0) + Bome Midi Translator Pro if needed)

### 1. Sound Card (Macbook Pro)

#### External Headphone jack

This setup is for the internal sound card on my Macbook Pro. I also own a Native Instruments Z1 which contains its own sound card, providing a separate stereo pair for monitoring.

### 2. Virtual Sound Card (Loopback)

Loopback allows additional stereo pairs to be added to an existing sound card. These pairs can then be used for internal routing via input and output settings in Traktor and Live.

Some web tutorials use Jack Audio instead. I prefer Loopback’s routing UI.

#### Devices

1. Click *+ New Virtual Device*
2. Click the pencil icon next to the title
3. Rename to *Loopback - Mac SC + Traktor + Live*

#### Sources

1. Click *+*
2. Select *Pass-Thru*
3. By default this has 2 channels: (1+2 / L+R). To add additional channels, use *Output Channels*.

#### Output Channels

1. The Pass-Thru source adds 2 channels by default (1+2 / L+R)
2. Click +, +, +
3. Six channels are added (3+4, 5+6, 7+8)
4. Click on each of the cables for 7+8 and click the Delete button
5. Drag new 7+8 cables from 7+8 to 5+6. This serves to output Traktor’s cue channel to the master, as this configuration is not possible in Traktor.

These channels will be used as follows:

1. 1+2: Traktor Master Out
2. 3+4: Traktor Rec Out to Live In 
3. 5+6: Live Out to Traktor In
4. 7+8: Traktor metronome to Traktor In (to Master Out doesn’t work for some reason)

#### Monitors

1. None
2. Click Hide Monitors (bottom right)

---

### 3. DJ Application + MIDI Clock (Traktor)

#### Audio Setup

1. Audio Device: Loopback - Mac SC + Traktor + Live
2. Sample Rate: 44100 Hz
3. Buffer Size: 128

#### Output Routing

If the expected output pairs aren’t visible, restart Traktor.

1. Output Monitor: 7+8 from Loopback - Mac SC + Traktor + Live (this is for metronome syncing via Cue)
2. Output Master: 1+2 from Loopback - Mac SC + Traktor + Live
3. Output Record: 3+4 from Loopback - Mac SC + Traktor + Live

Note: “Headphones Mix” should also be set to 0 / off, otherwise there will be phasing in the master output and more noticeably in samples recorded in Live, due to Traktor’s output being routed back into the Deck D input.

#### Input Routing

If the expected input pairs aren’t visible, restart Traktor.

Deck D replaces Traktor’s Loop Recorder & Remix Decks with Live.

1. Input Deck A: not connected
2. Input Deck B: not connected
3. Input Deck C: not connected
4. Input Deck D: 5+6 from Loopback - Mac SC + Traktor + Live
5. Input FX Send: not connected
6. Input Aux: not connected

#### External Sync

1. External Clock Source: EXT
2. MIDI Clock Settings: Enable MIDI Clock

#### Loading

1. Resetting Controls: uncheck both as one or other can disrupt Sync slave (TODO add reference)

#### Decks Layout

Deck Flavour

1. A: Track Deck
2. B: Track Deck
3. C: Live Input (unused)
4. D: Live Input

#### Global Section (top of UI)

1. Offset: 0 Ms
2. Sync icon: On
3. Sync: push at first beat of bar to align Live’s 1.1.1 with Traktor’s beat grid (creates gap in audio)
4. Snap: On
5. Quant: On

#### Controller Manager

From tutorial: [How to Sync Ableton Live and Traktor - The Right Way | DJ Endo](https://www.youtube.com/watch?v=4xzldehIsCE)

##### Device Setup

1. Add: Generic MIDI
2. Edit Comment: CLOCK
3. Out-Port: Traktor Virtual Output

Then review other devices and make sure none are using an Out-Port of Traktor Virtual Output, or All.

#### Active Deck (to sample from)

1. Press MASTER so that the Master Clock Tempo in the Global Section matches the active deck’s BPM. This is what Live will sync to. Push Sync in Global Section to set the start of the bar.

---

### 4. Sampler & Sequencer (Live)

#### Audio

##### Audio Device

1. Driver Type: CoreAudio
2. Audio Input Device: Loopback - Mac SC + Traktor + Live (6 In, 6 Out)
3. Audio Output Device: Loopback - Mac SC + Traktor + Live (6 In, 6 Out)
4. Channel Configuration
   1. Input Config: Click 3/4 and type Traktor Out
   2. Output Config: Click 5/6 and type Traktor In

#### Link / MIDI

##### MIDI

1. Input: Traktor Virtual Output
   1. Track: On, Sync: On, Remote: On
   2. MIDI Clock Sync Delay
      1. Enable metronome in Traktor
      2. Enable Cue button on active deck
      3. Enable metronome in Live
      4. Track the slider until the metronomes are in sync

#### UI (top left)

##### Ext

1. Click Ext - Live will now follow the Sync source (Traktor Virtual Output)
2. Global launch quantisation: None (Punching in exactly when you want seems most reliable)

#### Tracks

#### Audio x4

1. Audio From: Ext. In, 3 / 4 Traktor Out
2. Monitor: Off
3. Audio To: Ext. Out 5 / 6 Traktor In

##### Master

1. Cue Out: 5 / 6 Traktor In (to sync metronomes)
2. Master Out: 5 / 6 Traktor In

#### Record from Traktor to Live

##### ClyphX Pro

This is used to reduce the number of button presses required to produce usable loops.

See tutorial: [Live Looping Setup - Hands Free! Ableton and ClyphX-Pro](https://www.youtube.com/watch?v=Yn_ExkefmCQ)

Audio tracks 1-4, as above

MIDI tracks 5-8, each contains 1x MIDI clip, named:

`[Rec N] all/arm off ; 1/arm ; 1/sel empty ; srecfix 4 ;`

1. Unarm all tracks
2. Arm Audio track N (e.g. 1)
3. Select an empty slot in Audio track N, creating a new scene if necessary
4. Set the session (clip) record length to 4 bars, start and end the recording, start playback

TODO: Map clip nudge buttons or process offset in ClyphX or offset audio somehow as slightly behind Traktor

---

### 5. Controller Mapping

#### nanoKONTROL Studio

Mapped via the Traktor TSI Korg nanoKONTROL Studio v2.2 and Korg KONTROL Editor config.nktrl_st_set

Controls in channels 5-8 are mapped directly to Ableton Live. Buttons automatically light up to match the corresponding state in Ableton Live.

Select buttons 5-8 are mapped to the ClyphX [Rec N] buttons in MIDI tracks 5-8 of Ableton Live. This allows them to trigger sequences of actions in Ableton Live.

TOOD: I believe this only works / shows up in Traktor because Traktor Virtual Input is enabled?

#### nanoKEY Studio

Mapped via the Traktor TSI Korg nanoKEY Studio v1

#### ClyphX Pro

ClyphX Pro can be used to trigger MIDI control value changes in Traktor, e.g.

`[Move control to left then center] MIDI CC 1 50 0 ; WAITS 4B ; MIDI CC 1 50 64 ;`

1. Move control Ch 01. CC 50 to value 0 (full left)
2. Wait 4 bars
3. Move control Ch 01. CC 50 to value 64 (half way)

Ch 01. CC 50 could then be mapped to a Gain control, Crossfader etc in Traktor.

Setup in Traktor:

1. Use my Traktor-ClyphX.tsi
2. In-Port: Traktor Virtual Input
3. Out-Port: None 
4. Map controller input to Traktor element in this TSI

Setup in Ableton Live:

1. Control Surface > ClyphX Pro - Set Output to: Traktor Virtual Input
2. Output: ClyphX_Pro Output: Track: On, Remote: On

---

## Files

### ableton-live

Starter file for four channel sampler.

### clyphx-pro

Configuration files for Isotonik Studios / Stray's ClyphX Pro, which map MIDI controls to Live's interface and provide LED feedback.

* `/Users/Dan/NativeKONTROL/ClyphX_Pro/Button Bindings.txt`
* `/Users/Dan/NativeKONTROL/ClyphX_Pro/X-Controls.txt`
* `/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions/SelectedTrackLedStates.py`

### korg-kontrol-editor

Configuration file for the control surface editor.

### svg-overlays

SVG designs which can be print and cut to create custom overlays for the hardware.

These are based on the PDF manuals avaiable from Korg:

* nanoKEY_studio_OM_E1b.pdf
* nanoKONTROL_Studio_OM_E1.pdf

### traktor-template

`.tsi` templates which map the control surface to Traktor's interface / API.
