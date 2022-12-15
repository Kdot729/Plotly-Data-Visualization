import {disabled_icon} from "../disable.js"
import {check_website} from "../badges.js"

function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    $.getJSON({
        //Note Goes to fuction update_scatter_page() because it has /calling as route
        url: "/update_scatter_page",                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 

            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
                   
            empty_dropdowns();

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
            $(".selectpicker").selectpicker("refresh");
            disabled_icon(event);
            check_website($("#Website").val(), result["Badges"])

            //Note Reset the selected values for inequality dropdown
            if (event.target.id == "Reset-Icon")
            {
                reset_selected_inequality()
            }
        }
        })
    };
function empty_dropdowns()
{   
    $('#badge-area').empty();
    
    //! Forget what this does, but "Address" dropdown works. I think it removes all the options
    $("#Address option").remove();
};


function reset_selected_inequality()
{
    //Note Resest the selected value of each inequality since it's the default graph we can grab the zeroth index because it's the min and max
    $('#Less-Than').prop("selectedIndex", 0);
    $('#Greater-Than').prop("selectedIndex", 0);
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