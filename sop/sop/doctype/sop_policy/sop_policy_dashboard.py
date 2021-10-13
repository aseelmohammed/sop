from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'sop_policy',
		'transactions': [
			{
				'label': _('SOP Procedure'),
				'items': ['SOP Procedure']
			},
			{
				'label': _('SOP Form and Record'),
				'items': ['SOP Form and Record']
			}
		]
	}
