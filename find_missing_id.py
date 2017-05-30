def find_missing_id(list):
	
    missing_id = 0
    
    for unique_id in list:
        if unique_id in missing_id:
        	missing_id = 0
    	else:
            missing_id = unique_id
            
    return missing_id
    
