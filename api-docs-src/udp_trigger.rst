UDP network trigger
===================

.. note:: This chapter is not part of the official Kinovea manual. It was compiled from the Kinovea source code (github.com/Kinovea/Kinovea, commit ``13d0236``, October 2026) to document behavior the manual omits. Where the official manual and the source disagree, the source is what actually runs.

The capture screen can be triggered by a UDP packet, in addition to the audio trigger documented in *Recording triggers*. The official manual does not describe this.

Behavior
--------

* Kinovea listens on UDP port **8875** by default (configurable in the capture preferences, under the automation/trigger settings).
* **Any datagram** on that port fires the trigger. The payload is ignored entirely; an empty packet works.
* The trigger must be enabled (it is **off** by default) and armed on the capture screen.
* The configured trigger **quiet period** applies: packets arriving during it are ignored.
* The resulting action is the configured trigger action (default: record video).
* There is no authentication. Anyone on the network who can reach the port can start a recording; firewall accordingly.

Example sender
--------------

This is the test client shipped in the Kinovea repository (``Tools/remote/udp-client.py``), slightly generalized:

.. code-block:: python

    import socket

    def fire(host="192.168.0.228", port=8875):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # allows broadcast addresses too
        s.sendto(b"", (host, port))
        s.close()

    fire()

Typical uses: a timing gate, force plate or microcontroller (ESP32, Arduino with Ethernet) signalling the moment of interest. Combine with the capture delay buffer so the recording includes the moments *before* the trigger.
