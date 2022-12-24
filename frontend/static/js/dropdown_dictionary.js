function standard_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    console.log(split_url)
    return {
        "Graph": split_url[4],                             //Note Using the url to get the Graph Type
        "Specificity": split_url[5], 
        "Tool": split_url[6],                                 //Note Using the url to get the Tool
        "ID of Dropdown": event.target.id,                    //Note Might Use these to fix the dropdowns later
        "Type": $("#Type").val()
            }
}


function date_specific_dictionary()
    {
    return {
        "Start Date": $("#Start-Date").val(),                    //Note Using JQuery to get Start-Date value
        "End Date": $("#End-Date").val(),                        //Note Using JQuery to get End-Date value 
            }
    }

function address_specific_dictionary()
    {
    return {
        "Chosen Addresses": ($("#Address").val()).toString(),  //Note Using JQuery to get Address value, then converting to string
            }
    }


function inequality_specific_dictionary()
    {
    return {
        "Less Than": $("select#Less-Than").val(),               //Note Using JQuery to get Less-Than selected value
        "Greater Than": $("select#Greater-Than").val(),          //Note Using JQuery to get Greater-Than selected value
            }
    }

export {standard_dictionary, 
        date_specific_dictionary, 
        address_specific_dictionary, 
        inequality_specific_dictionary, 
        }