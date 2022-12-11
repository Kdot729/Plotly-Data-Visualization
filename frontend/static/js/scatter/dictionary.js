import * as dictionary from "../dropdown_dictionary.js"
 

function initilize_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    
    let standard_dropdown_dictionary = dictionary.standard_dictionary(event, split_url)

    
    if (split_url[4] == "basic")
    {

        let new_dictionary = check_ID(standard_dropdown_dictionary["ID of Dropdown"]) 
        
        //Note Combine both dictionaries into one
        return Object.assign({}, standard_dropdown_dictionary, new_dictionary);
    }   
}

function check_ID(ID){

    if ((ID == "Start-Date") || (ID == "End-Date"))
    {
        return dictionary.date_specific_dictionary()
    }

    else if (ID == "Address")
    {
        return dictionary.address_specific_dictionary()
    }

    else if (ID == "Type-Address")
    {
        return dictionary.type_address_specific_dictionary()
    }

    else if ((ID == "Less-Than") || (ID == "Greater-Than"))
    {
        return dictionary.inequality_specific_dictionary()
    }
    
    else if (ID == "Reset-Icon")
    {
        return dictionary.reset_specific_dictionary()
    }

}

export {initilize_dictionary}