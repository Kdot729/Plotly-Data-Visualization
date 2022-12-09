function initilize_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    
    let standard_dropdown_dictionary = 
    {
        "Graph": split_url[3],                             //* Using the url to get the Graph Type
        "Specificity": split_url[4], 
        "Tool": split_url[5],                                    //* Using the url to get the Tool
        "ID of Dropdown": event.target.id                    //* Might Use these to fix the dropdowns later
    }
    
    if (split_url[4] == "basic")
    {

        let new_dictionary = check_ID(standard_dropdown_dictionary["ID of Dropdown"])
        let finished_dictionary = Object.assign({}, standard_dropdown_dictionary, new_dictionary);  
        
        return finished_dictionary
    }   
}

function check_ID(ID){

    if ((ID == "Start-Date") || (ID == "End-Date"))
    {
        let specific_dictionary = 
        {
            "Start_Date": $("#Start-Date").val(),                    //* Using JQuery to get Start-Date value
            "End_Date": $("#End-Date").val(),                        //* Using JQuery to get End-Date value
            "Address_Type": $("#Type-Address").val()
        }
        return specific_dictionary
    }

    else if (ID == "Address")
    {
        let specific_dictionary = 
        {
            "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
            "Address_Type": $("#Type-Address").val()
        }
        return specific_dictionary
    }

    else if (ID == "Type-Address")
    {
        let specific_dictionary = 
        {
            "Address_Type": $("#Type-Address").val()               //* Using JQuery to get Type-Address value
        }
        return specific_dictionary
    }


    else if ((ID == "Less-Than") || (ID == "Greater-Than"))
    {
        let specific_dictionary = 
        {
            "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
            "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
            "Address_Type": $("#Type-Address").val()

        }
        return specific_dictionary
    }
    else if (ID == "Reset-Icon")
    {
        let specific_dictionary = 
        {
            "Address_Type": $("#Type-Address").val()               //* Using JQuery to get Type-Address value
        }
        return specific_dictionary
    }

}