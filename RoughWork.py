o={1, 2}
oo=[1,2,4]

lll=[{'permission_id': 1, 'permission_name': 'can_view_test'},\
     {'permission_id': 2, 'permission_name': 'can_edit_test'}, 
     {'permission_id': 4, 'permission_name': 'can_delete_test'}]

new_list=[]
dict_perm_with_true = {}
for  item in lll:
        dict_perm_with_true["permission_id"]=item["permission_id"]
        dict_perm_with_true["permission_name"]=item["permission_name"]

        if item["permission_id"] in o:
            dict_perm_with_true["InThisRole"]  = True
        else:
            dict_perm_with_true["InThisRole"] = False

        new_list.append(dict_perm_with_true.copy())
        

print(new_list)
