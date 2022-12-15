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
        "Start Date": $("#Start-Date").val(),                    //Note Using JQuery to get Start-Date value
        "End Date": $("#End-Date").val(),                        //Note Using JQuery to get End-Date value
        "Type": $("#Type").val()
            }
    }

function address_specific_dictionary()
    {
    return {
        "Chosen Addresses": ($("#Address").val()).toString(),  //Note Using JQuery to get Address value, then converting to string
        "Type": $("#Type").val()
            }
    }

function type_specific_dictionary()
    {
    return {
        "Type": $("#Type").val()               //Note Using JQuery to get Type value
            }
    }

function inequality_specific_dictionary()
    {
    return {
        "Less Than": $("select#Less-Than").val(),               //Note Using JQuery to get Less-Than selected value
        "Greater Than": $("select#Greater-Than").val(),          //Note Using JQuery to get Greater-Than selected value
        "Type": $("#Type").val()
            }
    }

function reset_specific_dictionary()
    {
    //Note Resest the selected value of each inequality since it's the default graph we can grab the zeroth index because it's the min and max
    $('#Less-Than').prop("selectedIndex", 0);
    $('#Greater-Than').prop("selectedIndex", 0);

    return {
        "Type": $("#Type").val()               //Note Using JQuery to get Type value
            }
    }

export {standard_dictionary, 
    date_specific_dictionary, 
    address_specific_dictionary, 
    type_specific_dictionary, 
    inequality_specific_dictionary, 
    reset_specific_dictionary}