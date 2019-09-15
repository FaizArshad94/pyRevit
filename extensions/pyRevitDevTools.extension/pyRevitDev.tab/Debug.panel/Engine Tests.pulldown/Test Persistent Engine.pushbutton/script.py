"""Testing non-modal windows calling actions thru external events.

Shift-Click:
Run window as Modal
"""
# pylint: skip-file
from pyrevit import forms
from pyrevit import UI
from pyrevit.runtime import types as runtime_types


class NonModalWindow(forms.WPFWindow):
    def __init__(self, xaml_file_name, ext_event, ext_event_handler):
        forms.WPFWindow.__init__(self, xaml_file_name)
        self.ext_event = ext_event
        self.ext_event_handler = ext_event_handler
        self.prev_title = "Title Changed..."

    def action(self, sender, args):
        if __shiftclick__:
            self.Close()
            forms.alert("Stuff")
        else:
            self.ext_event_handler.KeynoteKey = "12"
            self.ext_event_handler.KeynoteType = UI.PostableCommand.UserKeynote
            self.ext_event.Raise()

    def other_action(self, sender, args):
        self.Title, self.prev_title = self.prev_title, self.Title


handler = runtime_types.PlaceKeynoteExternalEventHandler()

NonModalWindow(
    'NonModalWindow.xaml',
    ext_event=UI.ExternalEvent.Create(handler),
    ext_event_handler=handler
    ).show(modal=__shiftclick__)