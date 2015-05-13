"""
Created: 11.05.2014
Last modified: 11.05.2014

Author: crasbe
"""

import classes.plugins.plugin as plugin

class Channel(plugin.Plugin):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        plugin.Plugin.__init__(self)
        
        self.plugins.update({"?haus" : self.haus})
