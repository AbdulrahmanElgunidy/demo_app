# Copyright (c) 2024, support and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):

	@frappe.whitelist()
	def frm_call(self,msg):
		import time 
		time.sleep(5)
		self.mo_no = 1061236286

		#return "Hi this message from frm_call"





















	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data=frappe.db.sql("""

	# 						select 
	# 				 			first_name,
	# 							age
	# 				 		FROM
	# 				 			`tabClient Side Scripting`
	# 				 		WHERE
	# 				 			enable=1			

	# 					""",as_dict=1)
	# 	for d in data :
	# 		frappe.msgprint(frappe._("The parent first name is {0} and age is {1}").format(d.first_name,d.age))



















	# # frappe.db.count(doctype,filters)
	# # count the documents
	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting',{'enable':1})
	# 	frappe.msgprint(frappe._("The enable Document count is {0}").format(doc_count))



















	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','PR-0018'):
	# 		frappe.msgprint(frappe._("The document is exist in database"))
	# 	else:		   
	# 		frappe.msgprint(frappe._("The document dose not exists in Database"))











	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','PR-0015','age',25)
	# 	first_name,age=frappe.db.get_value('Client Side Scripting','PR-0015',['first_name','age'])
	# 	self.first_name = first_name
	# 	self.age = age
	# 	frappe.msgprint(frappe._("The Parent First Name is {0} and new age is {1} ").format(first_name,age))
























	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc=frappe.db.get_list('Client Side Scripting',
	# 					 filters={
	# 						 'enable':1
	# 					 },
	# 					 fields=['first_name','age']
	# 					 )

	# 	for d in doc:
	# 		frappe.msgprint(frappe._("The parent First Name is {0}and age is{1}").format(d.first_name,d.age))












      

	# #Save Document
	# def save_document(self):
	# 	doc=frappe.new_doc('Client Side Scripting')
	# 	doc.first_name='dany'
	# 	doc.age=31
	# 	doc.save()
	    
	# 	doc.save(
	# 		 ignore_permession= True,
	#          ignore_version=True
	# 		 )

	# ## Delete document first option 
	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR-0008')  

	# ## Delete document second  option
	# def delete_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting','PR-0002')
	# 	doc.delete()

	# def validate(self):
	# 	self.db_set_document()



	# ## Set value into document
	# def db_set_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting','PR-0004')
	# 	doc.db_set('age',45)	







    # def validate(self):
    #     self.new_document()
    # def new_document(self):
        
    #     doc=frappe.new_doc('Client Side Scripting')
    #     doc.first_name='jake'
    #     doc.last_name='jay'
    #     doc.age=13
        
    #     doc.append("family_members",{
    #         "name1":"abdo",
    #         "relation":"friend",
    #         "age":14
	# 	})
        
    #     doc.insert()
        
        
    




















# ## fetch document and child doc values 
# 	def validate(self):
# 		self.get_document()

# 	def get_document(self):
# 		doc=frappe.get_doc('Client Side Scripting',self.client_side_doc)
# 		frappe.msgprint(frappe._("The First name is {0} and age is {1}").format(doc.first_name,doc.age))

# 		for row in doc.get("family_members"):
# 			frappe.msgprint(frappe._("{0}. The family member name is '{1}' and relation is '{2}'")).format(row.idx,row.name1,row.relation)




	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(frappe._(
	# 			"{0}. The family member Name is '{1}' and Relation is '{2}'"
	# 		).format(row.idx, row.name1, row.relation))



# def validate(self):
# 	frappe.msgprint(_("Hello my full_name is '{0}'").format(
# 		self.first_name+" "+self.middle_name+" "+self.last_name))



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#############################################################
	
	# def validate (self):
	# 	frappe.msgprint("Hello Frappe")

	# def before_save (self):
	# 		frappe.throw("Hello Frappe from before save event")
    
	# def before_insert (self):
	# 		frappe.throw("Hello Frappe from after insert event")	
    

	# def on_update (self):
	# 		frappe.throw("Hello Frappe from on update event")		
    
	# def before_submit (self):
	# 		frappe.throw("Hello Frappe from beforesubmit event")		

	# def on_submit (self):
	# 		frappe.msgprint("Hello Frappe from on submit event")		

	# def on_trash (self):
	# 		frappe.throw("Hello Frappe from on trash event")		

	# def after_delete (self):
	# 		frappe.throw("Hello Frappe from after delete event")		
