import {disabled_icon} from "../disable.js"
import {link_website} from "../badges.js"
import {repopulate_address_dropdown, repopulate_inequality_dropdowns, reset_selected_inequality} from "../dropdown_functions.js"

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
            // $("#Less-Than").empty();
            // $("#Greater-Than").empty();
        
            // //! Forget what this does, but "Address" dropdown works. I think it removes all the options
            $("#Address option").remove();

            if (event.target.id == "Type")
            {
                $("#Less-Than").empty();
                $("#Greater-Than").empty();
                repopulate_inequality_dropdowns("#Less-Than", result["Descending List"])
                repopulate_inequality_dropdowns("#Greater-Than", result["Ascending List"])
  
            }

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
            link_website($("#Website").val(), result["Badges"])

            //Note Reset the selected values for inequality dropdown
            if (event.target.id == "Reset-Icon")
            {
                reset_selected_inequality()
            }
        }
        })
    };

export {update_graph_and_dropdowns}