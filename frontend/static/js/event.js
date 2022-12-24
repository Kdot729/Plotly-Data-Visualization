import {repopulate_address_dropdown, repopulate_inequality_dropdowns, reset_selected_inequality, reset_date} from "./dropdown_functions.js"

function event_checker(event_id, result, dropdown_dictionary)
{
    if (event_id == "Type")
        {
            type_event(result["Descending List"], result["Ascending List"])
            address_event(result, dropdown_dictionary)
        }

    else if (event_id == "Address")
        {address_event(result, dropdown_dictionary)}

    //Note Reset the selected values for inequality dropdown
    else if (event_id == "Reset-Icon")
        {
            reset_date()
            reset_selected_inequality()
            address_event(result, dropdown_dictionary)
        }
}

function type_event(desc_list, asc_list)
{
    $("#Less-Than").empty();
    $("#Greater-Than").empty();
    repopulate_inequality_dropdowns("#Less-Than", desc_list)
    repopulate_inequality_dropdowns("#Greater-Than", asc_list)
}

function address_event(result, dropdown_dictionary)
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