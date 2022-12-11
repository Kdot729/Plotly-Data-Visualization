function standard_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    

    return {
        "Graph": split_url[3],                             //Note Using the url to get the Graph Type
        "Specificity": split_url[4], 
        "Tool": split_url[5],                                 //Note Using the url to get the Tool
        "ID of Dropdown": event.target.id                    //Note Might Use these to fix the dropdowns later
            }
}


function date_specific_dictionary()
    {
    return {
        "Start_Date": $("#Start-Date").val(),                    //Note Using JQuery to get Start-Date value
        "End_Date": $("#End-Date").val(),                        //Note Using JQuery to get End-Date value
        "Address_Type": $("#Type-Address").val()
            }
    }

function address_specific_dictionary()
    {
    return {
        "Chosen_Addresses": ($("#Address").val()).toString(),  //Note Using JQuery to get Address value, then converting to string
        "Address_Type": $("#Type-Address").val()
            }
    }

function type_address_specific_dictionary()
    {
    return {
        "Address_Type": $("#Type-Address").val()               //Note Using JQuery to get Type-Address value
            }
    }

function inequality_specific_dictionary()
    {
    return {
        "Less_Than": $("select#Less-Than").val(),               //Note Using JQuery to get Less-Than selected value
        "Greater_Than": $("select#Greater-Than").val(),          //Note Using JQuery to get Greater-Than selected value
        "Address_Type": $("#Type-Address").val()
            }
    }

function reset_specific_dictionary()
    {
    return {
        "Address_Type": $("#Type-Address").val()               //Note Using JQuery to get Type-Address value
            }
    }

export {standard_dictionary, 
    date_specific_dictionary, 
    address_specific_dictionary, 
    type_address_specific_dictionary, 
    inequality_specific_dictionary, 
    reset_specific_dictionary}