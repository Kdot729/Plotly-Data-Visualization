import {disabled_icon} from "./disable.js"
import {link_website} from "./badges.js"
import {always_empty} from "./dropdown_functions.js"
import {event_checker} from "./event.js"
import {question_mark_ping} from "./reveal.js"

function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    $.getJSON({
        //Note Goes to fuction update_page_router() because it has /calling as route
        url: "/update_page_router",                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 

            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
            question_mark_ping(event.target.id)
            always_empty()

            event_checker(event.target.id, result, dropdown_dictionary)

            $(".selectpicker").selectpicker("refresh");

            disabled_icon(event);

            link_website($("#Website").val(), result["Badges"])

        }
        })
    };

export {update_graph_and_dropdowns}