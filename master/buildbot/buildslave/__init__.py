# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

# This module is left for backward compatibility of old-named worker API.
# It should never be imported by Buildbot.

from buildbot.worker_transition import _on_old_name_usage

_on_old_name_usage(
    "'{old}' module is deprecated, use "
    "'buildbot.worker' module instead".format(old=__name__))

from buildbot.buildslave.base import AbstractBuildSlave
from buildbot.buildslave.base import AbstractLatentBuildSlave
from buildbot.buildslave.base import BuildSlave

__all__ = ("AbstractBuildSlave", "BuildSlave", "AbstractLatentBuildSlave")