# -*- Encoding: UTF-8 -*-
# Copyright (c) 2008 Henri Häkkinen
#
# This file is part of the UbuntuMan Supybot IRC plugin.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Provides commands for displaying UNIX manual pages from the Ubuntu Manpage
Repository.
"""

from imp import reload
import supybot
import supybot.world as world

__version__ = '1.2.1'

__author__ = supybot.Author('Henri Hakkinen', 'henux', 'henux@users.sourceforge.net')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {supybot.Author('Terence Simpson', 'stdin', ''): '',
                    supybot.Author('Elián Hanisch', 'm4v', 'lambdae2@gmail.com'): ''}

# This is a url where the most recent plugin package can be downloaded.
__url__ = 'http://henux.nor.fi/projects/ubuntuman.php'
 # 'http://supybot.com/Members/yourname/UbuntuMan/download'

from . import config
from . import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
