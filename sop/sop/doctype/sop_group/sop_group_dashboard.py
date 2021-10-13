from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'sop_group',
		'transactions': [
			{
				'label': _('SOP Category'),
				'items': ['SOP Category']
			},
			{
				'label': _('SOP Job Description'),
				'items': ['SOP Job Description']
			}
		]
	}
