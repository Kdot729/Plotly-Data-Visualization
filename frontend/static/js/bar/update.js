import {disabled_icon} from "../disable.js"
import {link_website} from "../badges.js"
import {repopulate_address_dropdown, repopulate_inequality_dropdowns, reset_selected_inequality} from "../dropdown_functions.js"
import {event_checker} from "./event.js"

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
            
            //Note Remove all the options in the "Address" dropdown
            $("#Address option").remove();

            event_checker(event.target.id, result, dropdown_dictionary)

            $(".selectpicker").selectpicker("refresh");

            disabled_icon(event);

            link_website($("#Website").val(), result["Badges"])

        }
        })
    };

export {update_graph_and_dropdowns}