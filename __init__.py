# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SearchArch
                                 A QGIS plugin
 This plugin is designed to search for archaeological sites on a dedicated area.
                             -------------------
        begin                : 2018-06-02
        copyright            : (C) 2018 by Grickevich
        email                : grickevich-marina@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SearchArch class from file SearchArch.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .search_arch import SearchArch
    return SearchArch(iface)
