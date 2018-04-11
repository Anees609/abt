from __future__ import unicode_literals
from frappe import _

def get_notification_config():
	return {
		"for_doctype": {
			"Backup Strategy": {"status": "Active"},
				}
	}
