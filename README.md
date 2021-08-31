# traktor-template-nk

[![GitHub release](https://img.shields.io/github/v/tag/dotherightthing/traktor-template-nk)](https://github.com/dotherightthing/traktor-template-nk/releases) [![GitHub issues](https://img.shields.io/github/issues/dotherightthing/traktor-template-nk.svg)](https://github.com/dotherightthing/traktor-template-nk/issues)

Traktor template for KORG nanoKONTROL + nanoKEY Studio.

Includes Live starter file with Traktor mixer and 4 channel Live sampler.

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

1. **[Physical Sound Card](#1-physical-sound-card):**
    * Macbook Pro (15-inch, 2018 / macOS v10.15.7)
    * External Headphones (headphones or [Minirig](https://www.minirig.co.nz/) plugged into headphone jack)
2. **[Virtual Sound Card](#2-virtual-sound-card):**
    * [Rogue Amoeba Loopback](https://rogueamoeba.com/loopback/) (v2)
3. **[DJ Application and MIDI Clock](#3-dj-application-and-midi-clock):**
    * [Native Instruments Traktor Pro 3](https://www.native-instruments.com/en/products/traktor/dj-software/traktor-pro-3/) (v3.4.2)
4. **[Mixer and Sampler](#4-mixer-and-sampler):**
    * [Ableton Live](https://www.ableton.com/en/live/) (v10) + ClyphX Pro (v1.2.0)
5. **[Controller Mapping](#5-controller-mapping):**
    * [KORG nanoKONTROL Studio](https://www.korg.com/us/products/computergear/nanokontrol_studio/) (v1.05)
    * [KORG nanoKEY Studio](https://www.korg.com/us/products/computergear/nanokey_studio/) (v1.08)
    * [KORG KONTROL Editor](https://www.korg.com/us/support/download/software/1/133/1355/)
    * [Native Instruments Traktor Controller Manager](https://support.native-instruments.com/hc/en-us/articles/209590569-How-to-Use-the-Controller-Manager-in-TRAKTOR) (part of Traktor Pro 3)
    * [Isotonik Studios ClyphX Pro](https://isotonikstudios.com/product/clyphx-pro/) (v1.2.0) (running in Ableton Live 10)
    * [Bome Midi Translator Pro](https://www.bome.com/products/miditranslator) (v1.9.0)
6. **[Mix Recorder](#6-mix-recorder):**
    * [Rogue Amoeba Audio Hijack](https://rogueamoeba.com/audiohijack/) (v3)
7. **[Launch script](#7-launch-script):**
    * [BetterTouchTool](https://folivora.ai/) (v3.570)
8. **[Configuration Files](#8-configuration-files)**
9. **[FAQs](#9-faqs)**

### 1. Physical Sound Card

This setup is for the internal sound card on my Macbook Pro. I also own a Native Instruments Z1 which contains its own sound card, providing a separate stereo pair for monitoring.

### 2. Virtual Sound Card

Loopback allows additional stereo pairs to be added to an existing sound card. These pairs can then be used for internal routing via input and output settings in Traktor and Live.

Some web tutorials use Jack Audio instead. I prefer Loopback’s routing UI.

![Screenshot of Loopback configuration](/loopback/loopback-config.png)

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

### 3. DJ Application and MIDI Clock

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

### 4. Mixer and Sampler

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

This controls MIDI sync, allowing Live's clock to sync to Traktor's clock.

* Control Surface: None
* Input: Traktor Virtual Output
  * Track: Off
  * Sync: On
  * Remote: Off
* Output: None

Takeover Mode: Value Scaling

Note: `MIDI Clock Sync Delay` was initially set using Traktor's internal mixer, with *Cue out* used to sync Traktor and Live's metronomes. Live now functions as the external mixer and syncing does not appear to be an issue anymore.

#### UI (top left)

##### Ext

1. Click Ext so that it lights up - Live will now follow the Sync source (Traktor Virtual Output) - if you have BetterTouchTool installed this will happen automatically
2. Global launch quantisation: None (Punching in exactly when you want seems most reliable)

#### Tracks

![Screenshot of Loopback configuration](/ableton-live/live-config.png)

##### Table

| Channel      | 1                           | 1FX      | 4FX      | 4                           | 5      | 6      | 7      | 8      | Master       |
|--------------|-----------------------------|----------|----------|-----------------------------|--------|--------|--------|--------|--------------|
| Audio From   | Ext. In: 3/4 Traktor Deck A | No Input | No Input | Ext. In: 5/6 Traktor Deck B | 1 PM   | 1 PM   | 1 PM   | 1 PM   | -            |
| Monitor      | In                          | In       | In       | In                          | Off    | Off    | Off    | Off    | -            |
| Audio To     | 1FX                         | Master   | Master   | 4FX                         | Master | Master | Master | Master | 1/2 Live Out |
| XFade assign | A                           | -        | -        | B                           | -      | -      | -      | -      | -            |

#### Record from Traktor to Live

ClyphX Pro is used to reduce the number of button presses required to produce usable loops.

I was initially inspired by this tutorial: [Live Looping Setup - Hands Free! Ableton and ClyphX-Pro](https://www.youtube.com/watch?v=Yn_ExkefmCQ)

Current workflow:

1. Press `Select` on Channel `1` or `4` (this sets the recording source to Traktor's Deck `A` or `B`)
2. Press `Select` on Channel `5`, `6`, `7`, `8` (this sets the target Live channel for sampling)
3. Press the `Record` button to start recording immediately
4. 4 bars of audio will be recorded

---

### 5. Controller Mapping

#### KORG nanoKONTROL Studio

Traktor config:

* Device: Korg nanoKONTROL Studio (`korg-nanokontrol-studio-v*.tsi` file)
* In-Port: nanoKONTROL Studio
* Out-Port: nanoKONTROL Studio
* Device Target: Focus

Live config:

* Control Surface: ClyphX Pro
* Input: nanoKONTROL Studio
  * Track: On
  * Sync: On (TODO: is this necessary?)
  * Remote: On
* Output: nanoKONTROL Studio
  * Track: On
  * Sync: Off
  * Remote: On

Controller config:

* Editor: KORG KONTROL Editor
* Set: `traktor-template-nk.nktrl_st_data`
* Data: `traktor-template-nk.nktrl_st_data`

#### KORG nanoKEY Studio

Traktor config:

* Device: Korg nanoKEY Studio (`korg-nanokey-studio-v*.tsi` file)
* In-Port: nanoKEY Studio
* Out-Port: nanoKEY Studio
* Device Target: Focus

Live config:

* Control Surface: ClyphX Pro XTA
* Input: nanoKEY Studio
  * Track: On
  * Sync: Off
  * Remote: On
* Output: nanoKEY Studio
  * Track: On
  * Sync: Off
  * Remote: On

Controller config:

* Editor: KORG KONTROL Editor
* Set: `traktor-template-nk.nanokey_st_set`
* Data: `traktor-template-nk.nanokey_st_data`

#### ClyphX Pro

ClyphX Pro is used to send messages to Traktor in action lists.

For example, the following action programmatically sends:

* a value of `127`
* to MIDI control change `46`
* on channel `16`
* via Live's Control Surface `ClyphX Pro XTB` (`MIDI` `B`) port
* which outputs MIDI messages to `Traktor Virtual Input`
* which sends the message to Traktor

`MIDIB CC 16 46 127`

This example allows controller-based track selection to be decoupled from Traktor deck selection when necessary.

Traktor setup:

* Device: `Traktor-ClyphX-Pro-v*1-0.tsi`
* In-Port: Traktor Virtual Input
* Out-Port: None
* Device Target: Focus

Manually map MIDI channel and CC in this template.

Live setup:

* Control Surface: ClyphX Pro XTB
* Input: None
* Output: Traktor Virtual Input
  * Track: Off
  * Sync: Off
  * Remote: Off

Controller config:

* N/A

#### Bome MIDI Translator Pro

Bome MIDI Translator Pro is used to filter MIDI messages from controllers before they reach Live.

Note: Bome needs to be running in the background.

Live setup:

* Control Surface: ClyphX Pro XTC
* Input: Bome MIDI Translator 1
  * Track: Off
  * Sync: Off
  * Remote: Off
* Output: None

Additional Bome functions:

1. Track 1-4 SELECT: Focus Traktor
2. Track 5-8 SELECT: Focus Live

--

### 6. Mix Recorder

While Ableton Live can be used record the evolving mix and any automation, the playback head jumps to 1.1.1 when Traktor is requested to send a Master Clock Sync message to Live.

This runs the risk of overwriting earlier recording later in the mix.

One solution is to use an external recording app, however free macOS apps provide limited control over what can be recorded.

For example, Quicktime can't distinguish between the individual channels used by the Loopback device, while [Audacity can only record all of them at once](https://forum.audacityteam.org/viewtopic.php?t=63424).

Audio Hijack offers two alternatives to this:

1. record directly from an application (e.g. Ableton Live)
2. record from specific virtual output channels (e.g. channels 1+2 of a Loopback device)

In addition Audio Hijack makes it clear when it is recording, by optionally displaying level meters in the [macOS menu bar](https://support.apple.com/en-nz/guide/mac-help/mchlp1446/10.15/mac/10.15).

---

### 7. Launch Script

BetterTouchTool (BTT) is a macOS app originally designed for customising the [Mac Touch Bar](https://support.apple.com/en-gb/guide/mac-help/mchlbfd5b039/10.15/mac/10.15) which appears on some Mac laptops.

BTT also provides controls over application launching and manipulation.

BTT solves various usability problems, such as:

* remembering to launch the different apps used in this template
* putting Live into External Sync mode
* starting the mix recorder

---

### 8. Configuration Files

#### ableton-live

Starter file with mixer and 4 channel sampler.

Automatically loaded by BetterTouchTool, otherwise double-click to load.

#### audio-hijack

Export of the configured session.

Automatically loaded by BetterTouchTool, otherwise double-click to load.

#### better-touch-tool

Export of the configured preset. Double-click this file to add the `Trakor NK` launch button to your Touch Bar.

#### bome-midi-translator-pro

Export of the configured project.

Automatically loaded by BetterTouchTool, otherwise double-click to load.

#### clyphx-pro (root folder and sub folders)

Configuration files for Isotonik Studio's / Stray's ClyphX Pro, which map MIDI controls to Live's interface and provides LED feedback.

[Symlink](https://gist.github.com/dotherightthing/3cbf17fe882dc8131eb8e9b9a501e9b9) the following files to their replacements in this repository:

| Replaced by a symlink                                          | Symlink target                                                                       |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------|
| /Users/You/NativeKONTROL/ClyphX_Pro/Button Bindings.txt      | traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/ClyphX_Pro/Button Bindings.txt  |
| /Users/You/NativeKONTROL/ClyphX_Pro/Encoder Bindings.txt     | traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/ClyphX_Pro/Encoder Bindings.txt |
| /Users/You/NativeKONTROL/ClyphX_Pro/G-Controls.txt           | traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/ClyphX_Pro/G Controls.txt       |
| /Users/You/NativeKONTROL/ClyphX_Pro/Macros.txt               | traktor-template-nk/clyphx-pro/ClyphX_Pro/Macros.txt                                   |
| /Users/You/NativeKONTROL/ClyphX_Pro/Preferences.txt          | traktor-template-nk/clyphx-pro/ClyphX_Pro/Preferences.txt                              |
| /Users/You/NativeKONTROL/ClyphX_Pro/Variables.txt            | traktor-template-nk/clyphx-pro/ClyphX_Pro/Variables.txt                                |
| /Users/You/NativeKONTROL/ClyphX_Pro/X-Controls.txt           | traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/ClyphX_Pro/X Controls.txt       |
| /Users/You/NativeKONTROL/ClyphX_Pro/XTA/Encoder Bindings.txt | traktor-template-nk/korg-nanokey-studio/clyphx-pro/ClyphX_Pro/XTA/Encoder Bindings.txt |
| /Users/You/NativeKONTROL/ClyphX_Pro/XTC/X-Controls.txt       | traktor-template-nk/bome-midi-translator-pro/clyphx-pro/ClyphX_Pro/XTC/X-Controls.txt  |

The following files need to be manually updated:

| Copy from                                                                                     | Copy to                                                                                                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/user_actions/SelectedTrackLedStates.py | /Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions/SelectedTrackLedStates.py |
| traktor-template-nk/korg-nanokontrol-studio/clyphx-pro/user_actions/SelectTraktorDeck.py      | /Applications/Ableton Live 10 Standard.app/Contents/App-Resources/MIDI Remote Scripts/ClyphX_Pro/clyphx_pro/user_actions/SelectTraktorDeck.py      |

#### korg-kontrol-editor (sub folders))

Configuration files for the control surface editor.

Double-click to open the set files.

Then choose Communication > Write Scene Data.

#### loopback

Screenshot of the 6-channel configuration. Loopback does not have an export feature.

#### svg-overlays (sub folders)

SVG designs which can be printed and cut to create custom overlays for the hardware.

These are based on the PDF manuals available from Korg:

* nanoKEY_studio_OM_E1b.pdf
* nanoKONTROL_Studio_OM_E1.pdf

#### traktor-template (sub folders)

`.tsi` templates which map the control surfaces to Traktor's interface / API.

---

### 9. FAQs

1. Why can't I hear recording clips in Live? - Press the sync button to sync playback with Traktor.
