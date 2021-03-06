# Created By: Virgil Dupras
# Created On: 2011/09/09
# Copyright 2013 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

def noop(*args, **kwargs):
    pass

class NoopGUI:
    def __getattr__(self, func_name):
        return noop

# A GUIObject is a cross-toolkit "model" representation of a GUI layer object, for example, a table.
# It acts as a cross-toolkit interface to multiple what we call here a "view". That view is a
# toolkit-specific controller to the actual view (an NSTableView, a QTableView, etc.).
# In our GUIObject, we need a reference to that toolkit-specific controller because some actions,
# have effects on it (for example, prompting it to refresh its data). The GUIObject is typically
# instantiated before its "view", that is why we set it as None on init. However, the GUI
# layer is supposed to set the view as soon as its toolkit-specific controller is instantiated.

# When you subclass GUIObject, you will likely want to update its view on instantiation. That
# is why we call self.view.refresh() in _view_updated(). If you need another type of action on
# view instantiation, just override the method.
class GUIObject:
    def __init__(self):
        self._view = None
    
    def _view_updated(self):
        pass #virtual
    
    def has_view(self):
        return (self._view is not None) and (not isinstance(self._view, NoopGUI))
    
    @property
    def view(self):
        return self._view
    
    @view.setter
    def view(self, value):
        # There's two times at which we set the view property: On initialization, where we set the
        # view that we'll use for your lifetime, and just before the view is deallocated. We need
        # to unset our view at that time to avoid calls to a deallocated instance (which means a
        # crash).
        if self._view is None:
            # Initial view assignment
            if value is None:
                return 
            self._view = value
            self._view_updated()
        else:
            assert value is None
            # Instead of None, we put a NoopGUI() there to avoid rogue view callback raising an
            # exception.
            self._view = NoopGUI()
    
