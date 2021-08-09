frappe.treeview_settings["SOP"] = {
	ignore_fields:["parent_sop"],
	get_tree_nodes: 'sop.sop.doctype.sop.sop.get_children',
	add_tree_node: 'sop.sop.doctype.sop.sop.add_node',
	breadcrumb: "SOP",
	root_label: "All SOP",
	get_tree_root: true,
	menu_items: [
		{
			label: __("New SOP"),
			action: function() {
				frappe.new_doc("SOP", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("SOP") !== -1'
		}
	],
	onload: function(treeview) {
		treeview.make_tree();
	},
	onrender: function(node) {
		if(1==1){

			// show Dr if positive since balance is calculated as debit - credit else show Cr
			let balance = node.data.balance_in_account_currency || node.data.balance;
			let dr_or_cr = balance > 0 ? "Dr": "Cr";

			if (node.data && node.data.type!==undefined) {
				if(node.data.type!='None')
				$('<span class="balance-area pull-right text-muted small">'
					+ node.data.type+ '</span>').insertBefore(node.$ul);
			}
		}
	},
};