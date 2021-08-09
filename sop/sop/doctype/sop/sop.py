# -*- coding: utf-8 -*-
# Copyright (c) 2021, Partner Consulting Solutions and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.nestedset import NestedSet, get_root_of
from erpnext.utilities.transaction_base import delete_events
from frappe.model.document import Document

class SOP(NestedSet):
	pass

@frappe.whitelist()
def get_children(doctype, parent=None, is_root=False):
	condition = ''
	var_dict = {
		"name": get_root_of("SOP"),
		"parent": parent
	}
	lan = frappe.db.get_value("User", frappe.session.user, "language")
	lang="name_{0}".format(lan)
	if parent:
		# args=dict(
		# 	reminder_text=reminder_text,
		# 	birthday_persons=birthday_persons,
		# 	message=message,
		# )
		condition = "parent_sop=%(parent)s"
	else:
		condition = "name=%(name)s"
	return frappe.db.sql("""
		select
			{lang} as title,
			name as value,
			type as type,
			is_group as expandable
		from `tab{doctype}`
		where
			{condition}
		order by name""".format(lang=lang,doctype=doctype, condition=condition), var_dict, as_dict=1)

@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args
	args = frappe.form_dict
	args = make_tree_args(**args)

	frappe.get_doc(args).insert()
