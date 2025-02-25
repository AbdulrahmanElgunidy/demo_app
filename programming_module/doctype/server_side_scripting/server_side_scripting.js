// Copyright (c) 2024, support and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server Side Scripting", {
    enable: function(frm) {
        frm.call({
            doc: frm.doc,
            method: 'frm_call',
            args: {
                msg: "hello"
            },
            freeze: true,
            freeze_message: __('calling frm_call Method'),
            callback: function(r) {
                frappe.msgprint(r.message);
            }
        });
    }
});
