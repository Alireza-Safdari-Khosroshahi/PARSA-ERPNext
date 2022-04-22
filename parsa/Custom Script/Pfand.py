import frappe
@frappe.whitelist()
def get_data_form_sql(item_code):
	ItemData = frappe.db.sql(f""" SELECT * FROM `tabItem` WHERE item_code='{item_code}' """, as_dict=True)
	if (ItemData[0].get("pfand_item")):
		pfandItemData = frappe.db.sql(f""" SELECT * FROM `tabItem` WHERE item_code='{ItemData[0].get("pfand_item")}' """, as_dict=True)	
		return pfandItemData
	else:
		return None
