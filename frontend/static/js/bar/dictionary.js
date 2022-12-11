import * as dictionary from "../dropdown_dictionary.js"

function initilize_dictionary(event)
{

    let standard_dictionary = dictionary.standard_dictionary(event)

    if (standard_dictionary["Specificity"] == "count_transactions")
    {
        let additional_dictionary = check_ID(standard_dictionary["ID of Dropdown"])

        //Note Combine both dictionaries into one
        return Object.assign({}, standard_dictionary, additional_dictionary);

    }
    
}

function check_ID(ID){

    if (ID == "Address")
    {
        return dictionary.address_specific_dictionary()
    }

    else if (ID == "Type")
    {
        return dictionary.type_specific_dictionary()
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