import {disabled_icon} from "../disable.js"
import {link_website} from "../badges.js"
import {event_checker} from "../event.js"
import {always_empty} from "../dropdown_functions.js"

function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    console.log(dropdown_dictionary["Graph"])
    console.log(`/update_scatter_page`)
    $.getJSON({
        //Note Goes to fuction update_page_router() because it has /calling as route
        // "/update_page_router"
        url: `/update_scatter_page`,                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 
            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
                   
            always_empty()

            event_checker(event.target.id, result, dropdown_dictionary)

            $(".selectpicker").selectpicker("refresh");

            disabled_icon(event);

            link_website($("#Website").val(), result["Badges"])

        }
        })
    };

export {update_graph_and_dropdowns}