#@osa-lang:AppleScript
# nk-traktor-live
# Traktor Pro mix template for the KORG nanoKEY/nanoKONTROL Studio MIDI controllers.
# https://github.com/dotherightthing/nk-traktor-live
#
# Note: when re-exporting, update the Short Version in the Bundle Info

property appRunCount : 0

on showAccessibilityPermissions()
	# See: https://forum.latenightsw.com/t/get-set-accessibility-permissions/1510/5
	tell application "System Preferences"
		activate

		set accessibilityPane to pane id "com.apple.preference.security"

		if current pane is not accessibilityPane then
			set current pane to accessibilityPane

			repeat while current pane is not accessibilityPane
				delay 0.25
			end repeat

			delay 0.25

		end if

		tell accessibilityPane to reveal anchor "Privacy_Accessibility"
	end tell
end showAccessibilityPermissions

on testAutomationPermissions()
	tell application "System Events"
		key code 27 # Escape
	end tell

	return true
end testAutomationPermissions

on getAppName(appFileName)
	tell application "Finder"
		set input to (POSIX path of (container of (path to me) as alias))
	end tell

	set appInfo to info for (POSIX path of input) & appFileName as POSIX file

	return name of appInfo
end getAppName

on getAppVersion(appFileName)
	tell application "Finder"
		set input to (POSIX path of (container of (path to me) as alias))
	end tell

	set appInfo to info for (POSIX path of input) & appFileName as POSIX file

	return short version of appInfo
end getAppVersion

on removeAppFromAccessibilityPermissionsList(appFileName)
	do shell script "tccutil reset Accessibility `osascript -e 'id of app " & appFileName & "'`"
end removeAppFromAccessibilityPermissionsList

on getAppBundleId(appName)
	set appBundleId to do shell script "osascript -e " & ("id of application \"" & appName & "\"")'s quoted form & " || osascript -e " & ("id of application id \"" & appName & "\"")'s quoted form & " || :"

	return appBundleId
end getAppBundleId

on isAppInstalled(appBundleId)
	set doesExist to (appBundleId ≠ "")

	return doesExist
end isAppInstalled

on isAppRunning(appBundleId)
	tell application "System Events"
		set processIsRunning to ((bundle identifier of processes) contains appBundleId)
	end tell
end isAppRunning

on run
	set appFileName to "NK_Traktor_Live.app"

	# appRunCount only appears to update after a successful run
	set appRunCount to (appRunCount + 1)
	set appName to getAppName(appFileName)
	set appVersion to getAppVersion(appFileName)

	# flags for testing
	set audiohijack to true
	set bome to true
	set live to true
	set loopback to true
	set traktor to true

	set appHasPermissions to true

	set dialogTitle to appName & " (" & appVersion & ")"

	# --------------------------------------------------
	# Test app permissions
	# --------------------------------------------------

	# A. FIRST RUN
	#
	# 1. if the app is being run for the first time then an Accessibility permission checkbox will be added by macos;
	#     it will not be checked and the user will need to check it in order to to grant the app permissions;
	#    TODO THIS IS NOT WORKING ANYMORE
	#
	# B. SUBSEQUENT RUN
	#
	# if the app completed a successful run with no errors then it will determine that it is running for a second time;
	#
	# 1. if the source code has not changed, then the permissions checkbox will already be checked, if the user previously granted permissions;
	#
	# 2. if the source code has changed, then the checkbox will already be checked, if the user previously granted permissions, but permissions will be for the old source code;
	#   in this case the permissions will be reset via the commandline;
	#   running the app again will take the user to A1;
	#
	# EITHER RUN
	#
	# it's not possible to check if the checkbox is checked without first having assistive access, so the alert message covers both scenarios:
	# A1. not checked
	# B2. checked but revoked

	# TODO add while loop here?

	try
		set appHasPermissions to testAutomationPermissions()
	on error
		set appHasPermissions to false

		# A1 and B2
		showAccessibilityPermissions()

		set alertReply to display alert appFileName & " (" & appVersion & ")
needs permission to run:

System Preferences > Security & Privacy > Privacy > Accessibility

If " & appFileName & " is missing:

'Cancel' > Unlock > '+' > 'NK_Traktor_Live.app' > Lock > Re-run app

If " & appFileName & " is present and checked:

'Fix' > Unlock > '+' > 'NK_Traktor_Live.app' > Lock > Re-run app

If " & appFileName & "  is present and unchecked:

'Cancel' > Unlock > Check 'NK_Traktor_Live.app' > Lock > Re-run app

Run #" & appRunCount buttons {"Cancel", "Fix"} cancel button 1 default button 2
		if button returned of alertReply is equal to "Fix" then
			removeAppFromAccessibilityPermissionsList(appFileName)
		end if
	end try

	# --------------------------------------------------
	# App permissions granted
	# --------------------------------------------------

	if appHasPermissions then
		# See: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/DisplayDialogsandAlerts.html
		# See: https://applescript.fandom.com/wiki/Display_Dialog
		display dialog "Click 'Continue' to configure and run the following applications (if they are installed):

1. Rogue Amoeba Loopback
2. Bome MIDI Translator Pro
3. Native Instruments Traktor Pro
4. Ableton Live
5. Rogue Amoeba Audio Hijack
" with title ("NK Traktor Live (" & appVersion & ")") with icon note buttons {"Cancel", "Continue"} cancel button 1 default button 2


		# --------------------------------------------------
		# Folder selection
		# --------------------------------------------------

		# See: https://apple.stackexchange.com/questions/107179/get-current-path-to-script-within-applescript-and-append-subdirectory

		tell application "Finder"
			set input to (POSIX path of (container of container of (path to me) as alias))
		end tell

		# --------------------------------------------------
		# 1. Rogue Amoeba Loopback
		# --------------------------------------------------

		if loopback then
			set loopbackBundleId to getAppBundleId("Loopback")

			if isAppInstalled(loopbackBundleId) then
				if isAppRunning(loopbackBundleId) then
					tell application "Loopback"
						quit
					end tell
				end if

				set source to quoted form of ((POSIX path of input) & "loopback/Devices.plist")

				# https://stackoverflow.com/questions/23632885/open-users-library-folder-using-applescript
				set dest to quoted form of ((POSIX path of (path to application support folder from user domain as alias)) & "loopback")

				do shell script "cp " & source & " " & dest

				tell application "Loopback"
					activate
				end tell
			end if
		end if

		# --------------------------------------------------
		# 2. Bome MIDI Translator Pro
		# --------------------------------------------------

		if bome then
			tell application "Finder"
				open (POSIX path of input) & "bome-midi-translator-pro/nanoKONTROL Studio.bmtp" as POSIX file
			end tell

			# wait N seconds
			delay 2

			# The project has associated documentation in TXT format. Do you want to open it now? => No (n)
			# See: https://dougscripts.com/itunes/itinfo/keycodes.php
			tell application "System Events"
				tell application "Bome MIDI Translator Pro" to activate

				tell application "System Events"
					key code 45
				end tell
			end tell

			# wait N seconds
			delay 2
		end if

		# --------------------------------------------------
		# 3. Native Instruments Traktor Pro
		# --------------------------------------------------

		if traktor then
			tell application "Finder"
				open (POSIX path of input) & "traktor-pro/nk-traktor-live.tsi" as POSIX file
			end tell

			# wait N seconds
			delay 20
		end if

		# --------------------------------------------------
		# 4. Ableton Live
		# --------------------------------------------------

		if live and traktor then
			tell application "Finder"
				open (POSIX path of input) & "ableton-live/nk-traktor-live Project/nk-traktor-live.als" as POSIX file
			end tell

			# wait N seconds
			delay 15

			tell application "System Events"
				tell process "Live"
					click menu item "External Sync" of menu "Options" of menu bar 1
				end tell
			end tell
		end if

		# --------------------------------------------------
		# 5. Rogue Amoeba Audio Hijack
		# --------------------------------------------------

		if audiohijack then
			tell application "Finder"
				open (POSIX path of input) & "audio-hijack/nk-traktor-live.ahsession" as POSIX file
			end tell

			# wait N seconds
			delay 4

			# Control > Start Session (COMMAND+R)
			tell application "System Events"
				key code 15 using {command down}
			end tell
		end if

		# --------------------------------------------------
		# Maximise windows
		# --------------------------------------------------

		if live and traktor then
			# maximise window
			# See: https://stackoverflow.com/questions/1866912/applescript-how-to-get-current-display-resolution
			# See: https://daringfireball.net/2006/12/display_size_applescript_the_lazy_way
			# See: https://stackoverflow.com/a/20149022
			tell application "Finder"
				set _b to bounds of window of desktop
				set _width to item 3 of _b
				set _height to item 4 of _b

				tell application "System Events" to tell process "Live"
					set position of window 1 to {0, 0}
					set size of window 1 to {_width, _height}
				end tell

				tell application "System Events" to tell process "Traktor"
					set position of window 1 to {0, 0}
					set size of window 1 to {_width, _height}
				end tell
			end tell
		end if

		# --------------------------------------------------
		# Start MIDI Sync
		# --------------------------------------------------

		if live and traktor then
			# wait N seconds
			delay 2

			# Clock Send + Clock Trigger MIDI Sync (CONTROL+OPTION+COMMAND+S)
			# (mapped in Generic Keyboard device)
			tell application "System Events" to tell process "Traktor"
				key code 1 using {control down, option down, command down}
			end tell

			# wait N seconds
			delay 2
		end if
	end if
end run