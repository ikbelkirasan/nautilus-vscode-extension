"""
Author: Ikbel <https://github.com/ikbelkirasan>

Credits: Ricardo Rodrigues
"""
import os
from gi.repository import Nautilus, GObject


class VSCodeExtension(GObject.GObject, Nautilus.MenuProvider):
    """ Extension that allows for the quick open of VSCode in a file or folder """

    def __init__(self):
        pass

    def menu_activate_cb(self, menu, input_file):
        """ Method called when menu item is clicked """
        os.system('/usr/share/code/code --new-window ' +
                  input_file.get_location().get_path().replace(" ", "\\ "))

    def open_in_vscode(self, input_file):
        item = Nautilus.MenuItem(
            name="MimeTypeExtension::Show_File_Name",
            label="Open with VSCode",
            tip="Opens the file or folder with Visual Studio Code"
        )
        item.connect('activate', self.menu_activate_cb, input_file)

        return item

    def get_background_items(self, window, file):
        """ Method called when a right click occurs in the background """
        item = self.open_in_vscode(file)

        return item,

    def get_file_items(self, window, files):
        """ Method called when a right click occures in Nautilus """
        if len(files) != 1:
            return

        item = self.open_in_vscode(files[0])

        return item,
