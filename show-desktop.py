#!/usr/bin/python3

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as Gtk
from gi.repository.Wnck import Screen as Screen

screen = Screen.get_default()

# wait until we are allowed to process our event
while Gtk.events_pending():
    Gtk.main_iteration()

# toggle desktop
screen.toggle_showing_desktop(not screen.get_showing_desktop())


