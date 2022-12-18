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
            // $("#Less-Than").empty();
            // $("#Greater-Than").empty();
        
            // //! Forget what this does, but "Address" dropdown works. I think it removes all the options
            $("#Address option").remove();

            event_checker(event.target.id, result)

            $(".selectpicker").selectpicker("refresh");
            disabled_icon(event);
            link_website($("#Website").val(), result["Badges"])

        }
        })
    };

export {update_graph_and_dropdowns}