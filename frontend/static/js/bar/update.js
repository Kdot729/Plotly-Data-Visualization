import {disabled_icon} from "../disable.js"

function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    $.getJSON({
        //Note Goes to fuction update_bar_page() because it has /calling as route
        url: "/update_bar_page",                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 

            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
                   
            $('#badge-area').empty();


            //FIXME Need to pass in a new "Address" dropdown for when "Seller" is picked. Might have to use repopulate_address_dropdown()
            //FIXME Reset needs to clear the checkmark in the "Address" dropdpown
            $("#Address option").remove();

            //Note Check if the key "Chosen_Addresses" is in dropdown_dictionary
            if (("Chosen_Addresses" in dropdown_dictionary))
            {
                dropdown_dictionary["Chosen_Addresses"].split(',');
                repopulate_address_dropdown(result["Address List"], dropdown_dictionary["Chosen_Addresses"])
                
            }
            else
            {
                for(let i = 0; i < result["Address List"].length; i++) 
                {
                    $("#Address").append($("<option>").val(result["Address List"][i]).text(result["Address List"][i]));        
                }
                

            }
            $(".selectpicker").selectpicker("refresh");
            disabled_icon(event);
        }
        })
    };

function empty_dropdowns()
{   
    $('#badge-area').empty();
    // $("#Less-Than").empty();
    // $("#Greater-Than").empty();

    // //! Forget what this does, but "Address" dropdown works. I think it removes all the options
    // $("#Address option").remove();
};
function repopulate_inequality_dropdowns(selector_ID, inequality_list)
{
    for(let i = 0; i < inequality_list.length; i++)
        $("#" + selector_ID).append($("<option>").val(inequality_list[i]).text(inequality_list[i]));
}

function repopulate_address_dropdown(address_list, selected_addresses)
{
    for(let i = 0; i < address_list.length; i++) 
    {
            //Note This will recheck the address that were selected and if they meet all the requirements
            if (selected_addresses.includes(address_list[i])) 
                $("#Address").append($("<option selected>").val(address_list[i]).text(address_list[i]));

            else
                $("#Address").append($("<option>").val(address_list[i]).text(address_list[i]));        
     }
};
export {update_graph_and_dropdowns}