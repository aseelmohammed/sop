from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("SOP"),
			"items": [
				{
					"type": "doctype",
					"name": "SOP",
					"description":_("SOP"),
					"onboard": 1,
				},
			]
		},
	]