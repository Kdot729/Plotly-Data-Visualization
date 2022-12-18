import {repopulate_address_dropdown, repopulate_inequality_dropdowns, reset_selected_inequality} from "../dropdown_functions.js"

function event_checker(event_id, result)
{
    if (event_id == "Type")
        {type_event(result)}

    else if (event_id == "Address")
        {address_event(result)}

    //Note Reset the selected values for inequality dropdown
    else if (event_id == "Reset-Icon")
        {reset_selected_inequality()}
}

function type_event(result)
{
    $("#Less-Than").empty();
    $("#Greater-Than").empty();
    repopulate_inequality_dropdowns("#Less-Than", result["Descending List"])
    repopulate_inequality_dropdowns("#Greater-Than", result["Ascending List"])
}

function address_event(result)
{
    //Note Check if the key "Chosen Addresses" is in dropdown_dictionary
    if (("Chosen Addresses" in dropdown_dictionary))
    {
        dropdown_dictionary["Chosen Addresses"].split(',');
        repopulate_address_dropdown(result["Address List"], dropdown_dictionary["Chosen Addresses"])
        
    }
    else
    {
        for(let i = 0; i < result["Address List"].length; i++) 
        {
            $("#Address").append($("<option>").val(result["Address List"][i]).text(result["Address List"][i]));        
        }
    }
}

export {event_checker}