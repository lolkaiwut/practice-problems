def find_missing_id(list):
	
    missing_id = 0
    
    for unique_id in list:
        if unique_id in missing_id:
        	missing_id = 0
    	else:
            missing_id = unique_id
            
    return missing_id
    
def find_unique_delivery_id(delivery_ids):

    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id
