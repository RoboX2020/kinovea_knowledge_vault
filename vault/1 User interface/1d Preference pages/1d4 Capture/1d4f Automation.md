---
id: "1d4f"
title: "Automation"
aliases: ["Automation"]
tags: [kinovea, type/permanent, kinovea/user-interface]
up: "[[1d4 Capture]]"
source: official-manual
---

# Automation

![[capture_automation.png]]

## Audio trigger

### Enable audio trigger

When this option is checked Kinovea measures the volume level on the microphone and triggers the start of the recording when this volume goes above the configured threshold.

> [!note]
> The audio trigger mechanism can be disarmed for individual cameras from the capture screen controls.

### Input device

This option lets you select which microphone is used to trigger recordings.

> [!tip]
> Ensure that Kinovea can access your microphone by opening **Windows Sound settings**, going to **Microphone privacy settings** and turning on **Allow apps to access your microphone**.

### Trigger threshold

The trigger threshold defines the volume level required to trigger recordings. You should see the black line moving laterally as the microphone picks up sounds. The vertical red line represents the trigger level.

The counter on the right is incremented each time the trigger is reached and reset when the threshold value is changed. You can use this to get immediate feedback while figuring out the appropriate configuration.

### Idle time

The idle time defines the amount of time after each recording during which the audio trigger is automatically disarmed.

## Stop recording by duration

This option defines the maximum duration for recordings. Recordings started manually or by audio trigger will be stopped right after they reach this duration. Setting the value to 0 disables the option and requires manually stopping the recording process.

This option is orthogonal to delayed recording. For example if the camera is configured with a 2-second delay and the maximum duration is set to 5 seconds, the created video will last 5 seconds as configured: the first 2 seconds are actions that happened before the recording trigger and the last 3 seconds are actions that happened after the recording trigger.

In combination with the audio trigger this option lets you record multiple sequences without manually interacting with the computer.

> [!note]
> This value is a lower bound, the final video might be slightly longer than configured due to internal processing and alignment with frame boundaries.

## Ignore file overwrite warning

This option bypasses the overwrite confirmation dialog when the recording about to start points to an existing file. If the option is checked the existing file is irremediably deleted and overwritten by the new one.

This option can be used if you are limited in space and do not need to save all sequences. In this scenario you can continuously record to a single file and manually copy it to a different location only when you really want to keep it.

---
⬆ [[1d4 Capture]] · ⬅ [[1d4e Video naming]]
