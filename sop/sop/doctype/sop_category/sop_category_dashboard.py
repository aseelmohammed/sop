from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'sop_category',
		'transactions': [
			{
				'label': _('SOP Policy'),
				'items': ['SOP Policy']
			}
		]
	}
