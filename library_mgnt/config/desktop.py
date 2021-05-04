# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _
'''
def get_data():
	return [
		{
			"module_name": "Library Mgnt",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Library Mgnt")
		}
	]
	'''
def get_data():
    return {
        "Accounts": {
            "color": "#3498db",
            "icon": "octicon octicon-repo",
            "type": "module",
            "name":"Library_mgnt"

        },
    }


