// Copyright (c) 2024, support and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {

    //Value fetching 
    // 




    // refresh: function(frm) {

    //     // Adding a custom button 'Click Me1'
    //     frm.add_custom_button('Click Me1', () => {
    //         // Display a message when the button is clicked
    //         frappe.msgprint(__('You Clicked1 !!'));
    //     }, 'click me');
    
    //     // Adding another custom button 'Click Me2'
    //     frm.add_custom_button('Click Me2', () => {
    //         // Display a message when the button is clicked
    //         frappe.msgprint(__('You Clicked2 !!'));
    //     }, 'click me');
    // }
    












    // enable : function(frm){

    //     frm.set_df_property('first_name','reqd',1)
    //     // frm.refresh_field('first_name');
        
    //     frm.set_df_property('middle_name','read_only',1)
    //     // frm.refresh_field('middle_name');

    //     frm.toggle_reqd('age',true)

    // }












//   validate: function(frm){

//         //frappe.set_value('full_name',frm.doc.first_name + " " + frm.doc.middle_name+" "+frm.doc.last_name)

//         let row = frm.add_child('family_members',{
//             name1:'abr',
//             relation:'father',
//             age:56


//         }

//         )
//     }











    // refresh:function(frm){

    //     frm.set_intro('Now you can create a new client side scripting doctype')
    //     if (frm.is_new()){
    //         frm.set_intro('Now You can create a new client side scripting doctype')
    //     }
    // }













    //  after_save: function(frm){
    //     frappe.msgprint(__("The full name is '{0}' ",

    //         [frm.doc.first_name + " " + frm.doc.middle_name+" "+frm.doc.last_name ]

    //     ))

    //     for (let row of frm.doc.family_members ){
    //         frappe.msgprint(__("{0}. The Family member name is '{1}' and relation is '{2}'",
    //             [row.idx,row.name1,row.relation]

    //         ))

    //     }
                      
        
    // }
    



	// refresh(frm) {
    //     //frappe.msgprint("Hello Support")
    //     frappe.throw("This is an Error")

	// }
    
    
    // refresh: function(frm){

    //     frappe.msgprint("Hello Support refresh event")
    // }
    
    // onload: function(frm){
    // frappe.msgprint("Hello Support from onload event")
    // }

    // validate: function(frm){

    //     frappe.throw("Hello Support from Validate events")
    // }

    // before_save: function(frm){

    //     frappe.throw("Hello Support fom beforesave event")

    // }

   


    enable: function(frm){

        frappe.msgprint("Hell Support from Enable Field event")
    }

//   age: function(frm){

//     frappe.msgprint("Hello Support from age fieldname event")
//   }


// family_members_on_form_rendered: function(frm){

//     frappe.msgprint("Hello From Family member child table rendered event")
// }



// before_submit: function(frm){
//     frappe.throw("Hello Support before_submit event")
// }


//   on_submit: function(frm){

//     frappe.msgprint("Hello Support from on submit event")
//   }

// before_cancel: function(frm){
//     frappe.throw("Hello from before cancel event")
// }

//   after_cancel: function(frm){

//     frappe.msgprint("hello Support from after cancel event")
//   }
    ,
});





frappe.ui.form.on('Family Members',{

// name1:function(frm){

//     frappe.msgprint("Hello from child doctype name1 event")
// }


// age(frm,cdt,cdn){

//     frappe.msgprint("Hello from age child doctype fieldname event")
// }

})






































