# traktor-template-nk

[![GitHub release](https://img.shields.io/github/v/tag/dotherightthing/traktor-template-nk)](https://github.com/dotherightthing/traktor-template-nk/releases) [![GitHub issues](https://img.shields.io/github/issues/dotherightthing/traktor-template-nk.svg)](https://github.com/dotherightthing/traktor-template-nk/issues)

Traktor template for KORG nanoKONTROL + nanoKEY Studio.

Includes Live starter file with Traktor mixer and 5 channel Live sampler.

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
4. **Mixer, Sampler & Sequencer:** Ableton Live (v10) + ClyphX Pro (v1.2.0)
5. **Controller Mapping:** nanoKONTROL Studio + nanoKEY Studio + Traktor (v3.4.2) + KORG KONTROL Editor (+ Ableton Live (v10) + ClyphX Pro (v1.2.0) + Bome Midi Translator Pro if needed)

### 1. Sound Card (Macbook Pro)

#### External Headphone jack

This setup is for the internal sound card on my Macbook Pro. I also own a Native Instruments Z1 which contains its own sound card, providing a separate stereo pair for monitoring.

### 2. Virtual Sound Card (Loopback)

Loopback allows additional stereo pairs to be added to an existing sound card. These pairs can then be used for internal routing via input and output settings in Traktor and Live.

Some web tutorials use Jack Audio instead. I prefer Loopback’s routing UI.

#### Screenshot

![Screenshot of Loopback configuration](/screenshots/loopback-config.png)

#### Devices

1. Click *+ New Virtual Device*
2. Click the pencil icon next to the title
3. Rename to *Loopback - Mac SC + Traktor + Live*

#### Sources

1. Click *+*
2. Select *Pass-Thru*
3. By default this has 2 channels: (1+2 / L+R). To add additional channels, use *Output Channels*.

#### Output Channels

In order to be able to choose which Traktor deck to sample from, both decks must be routed to an external mixer.

This effectively means that Live becomes both the mixer (at least for deck volume control) and the sampler. This also means that recording mixes has to be done in Live, which is preferable anyway as retains the multitrack separation.

1. The Pass-Thru source adds 2 channels by default (1+2 / L+R)
2. Click `+` 2 times
3. 2 stereo channels are added (3+4, 5+6)

These channels will be used as follows:

1. 1+2: Live Out (to soundcard out)
2. 3+4: Traktor Deck A Out (to Live In)
3. 5+6: Traktor Deck B Out (to Live In)

#### Monitors

1. External Headphones, sourced from Output Channels 1+1

---

### 3. DJ Application + MIDI Clock (Traktor)

#### Audio Setup

1. Audio Device: Loopback - Mac SC + Traktor + Live
2. Sample Rate: 44100 Hz
3. Buffer Size: 128

#### Output Routing

If the expected output pairs aren’t visible, restart Traktor.

1. Mixing Mode: External
2. Output Deck A: 3+4 from Loopback - Mac SC + Traktor + Live
3. Output Deck B: 5+6 from Loopback - Mac SC + Traktor + Live
4. Output Deck C: not connected
5. Output Deck D: not connected
6. Output Preview: not connected
7. Output FX Return: not connected

Note: “Headphones Mix” should also be set to 0 / off, otherwise there will be phasing in the master output and more noticeably in samples recorded in Live, due to Traktor’s output being routed back into the Deck D input.

#### Input Routing

If the expected input pairs aren’t visible, restart Traktor.

1. Input Deck A: not connected
2. Input Deck B: not connected
3. Input Deck C: not connected
4. Input Deck D: not connected
5. Input FX Send (Ext): not connected

#### External Sync

1. External Clock Source: EXT
2. MIDI Clock Settings: Enable MIDI Clock

#### Loading

1. Resetting Controls: uncheck both as one or other can disrupt Sync slave (TODO add reference)

#### Decks Layout

Deck Flavour: 2 Decks

1. A: Track Deck / Advanced
2. B: Track Deck / Advanced

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

* Press MASTER so that the Master Clock Tempo in the Global Section matches the active deck’s BPM. This is what Live will sync to.
* Push Sync in Global Section to set the start of the bar.
* Select Sync on the other deck only, to ensure that new material matches the BPM.

---

### 4. Mixer, Sampler & Sequencer (Live)

#### Audio

##### Audio Device

1. Driver Type: CoreAudio
2. Audio Input Device: Loopback - Mac SC + Traktor + Live (6 In, 6 Out)
3. Audio Output Device: Loopback - Mac SC + Traktor + Live (6 In, 6 Out)
4. Channel Configuration
   1. Input Config:
      * 3/4: "Traktor Deck A"
      * 5/6: "Traktor Deck B"
   2. Output Config:
      * 1/2: "Live Out"

#### Link / MIDI

##### MIDI

1. Input: Traktor Virtual Output
   1. Track: On, Sync: On, Remote: On
   2. MIDI Clock Sync Delay: this was initially set using Traktor's internal mixer, with Cue out used to sync Traktor and Live's metronomes. However as Live now functions as the external mixer, syncing does not seem to be an issue anymore.

#### UI (top left)

##### Ext

1. Click Ext - Live will now follow the Sync source (Traktor Virtual Output)
2. Global launch quantisation: None (Punching in exactly when you want seems most reliable)

#### Tracks

##### Screenshot

![Screenshot of Loopback configuration](/screenshots/live-config.png)

##### Table

| Channel      | 1                           | FX       | 3                           | 4      | 5      | 6      | 7      | 8      | Master       |
|--------------|-----------------------------|----------|-----------------------------|--------|--------|--------|--------|--------|--------------|
| Audio From   | Ext. In: 3/4 Traktor Deck A | No Input | Ext. In: 5/6 Traktor Deck B | 1      | 1      | 1      | 1      | 1      | -            |
| Audio To     | Master                      | Master   | Master                      | Master | Master | Master | Master | Master | 1/2 Live Out |
| Monitor      | In                          | -        | In                          | Off    | Off    | Off    | Off    | Off    | -            |
| XFade assign | A                           | -        | B                           | -      | -      | -      | -      | -      | -            |

#### Record from Traktor to Live

##### ClyphX Pro

ClyphX Pro is used to reduce the number of button presses required to produce usable loops.

I was initially inspired by this tutorial: [Live Looping Setup - Hands Free! Ableton and ClyphX-Pro](https://www.youtube.com/watch?v=Yn_ExkefmCQ)

Current workflow:

1. Press `Select` on Channel `1` or `4` (this sets the recording source to Traktor's Deck `A` or `B`)
2. Press `Select` on Channel `5`, `6`, `7`, `8` (this sets the target Live channel for sampling)
3. Press the `Record` button to start recording immediately
4. 4 bars of audio will be recorded

---

### 5. Controller Mapping

#### nanoKONTROL Studio

Mapped via the Traktor TSI Korg nanoKONTROL Studio v2.2 and Korg KONTROL Editor config.nktrl_st_set

Controls in channels 1, 4, 5, 6, 7, 8 are mapped directly to Ableton Live. Buttons automatically light up to match the corresponding state in Ableton Live.

#### nanoKEY Studio

Mapped via the Traktor TSI Korg nanoKEY Studio v1

#### ClyphX Pro (Optional)

ClyphX Pro could optionally be used to trigger MIDI control value changes in Traktor, e.g.

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

Starter file with Traktor mixer and 5 channel Live sampler.

### clyphx-pro

Configuration files for Isotonik Studios / Stray's ClyphX Pro, which map MIDI controls to Live's interface and provide LED feedback.

* `/Users/Dan/NativeKONTROL/ClyphX_Pro/Button Bindings.txt`
* `/Users/Dan/NativeKONTROL/ClyphX_Pro/Encoder Bindings.txt`
* `/Users/Dan/NativeKONTROL/ClyphX_Pro/X-Controls.txt`
* `/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions/SelectedTrackLedStates.py`
* `/Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions/SetInputSource.py`

### korg-kontrol-editor

Configuration file for the control surface editor.

### svg-overlays

SVG designs which can be printed and cut to create custom overlays for the hardware.

These are based on the PDF manuals available from Korg:

* nanoKEY_studio_OM_E1b.pdf
* nanoKONTROL_Studio_OM_E1.pdf

### traktor-template

`.tsi` templates which map the control surface to Traktor's interface / API.

---

## Troubleshooting

1. Recording clips not heard in Live - Press the sync button to sync playback with Traktor.
