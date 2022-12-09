import {check_website} from "./link.js"

function disabled_dropdown(event) 
{
    //Note Select all "span" tag where the parent has a class "custom-tooltip"
    let tooltip_id_list = $.map($('.custom-tooltip > span'), span_id => span_id.id);

    // console.log("before condition",event.target.id)
    if (event.target.id == "Reset-Icon")
    {
        for(let i = 0; i < tooltip_id_list.length; i++)
        {
            let split_id = tooltip_id_list[i].split("Tooltip")[0]
            console.log("split", split_id)

            let button_id = split_id + "Icon-Button"
            let tooltip_id = split_id + "Tooltip"
            let icon_id = split_id + "Icon"

            //Note Get get of last character which is "-". Then replace the middle "-" with a space
            let tooltip_text = split_id.slice(0, -1).replaceAll("-", " ")
            
            //Note Makes button clickable
            $(`#${button_id}`).prop("disabled", false);

            //Note Changes tooltiptext to it's original text
            $(`#${tooltip_id}`).text(tooltip_text)
            
            //Note Changes icon color to it's original color
            $(`#${icon_id}`).css("color", "#004489")
        }

    }
    
    //Note "Type-Address" won't disable other icons
    else if ((event.target.id != "Reset-Icon") && (event.target.id != "Type-Address"))
    {
    
    //Note Passing tooltip id because it's the easiest to split
    for(let i = 0; i < tooltip_id_list.length; i++)
        {
            let split_id = tooltip_id_list[i].split("Tooltip")[0]
            
            // console.log(split_id)
            let button_id = split_id + "Icon-Button"
            let tooltip_id = split_id + "Tooltip"
            let icon_id = split_id + "Icon"

            // console.log(button_id, tooltip_id, icon_id)
            
            //Note Get get of last character which is "-" because event.target.id doesn't have a "-" 
            let conditional_id = split_id.slice(0, -1)
            // console.log("conditional", conditional_id)
            // console.log(event.target.id)

            //Note Harded coding that the "Website" and "Reset" icon don't get disabled
            //Note (event.target.id != conditional_id) makes it so the icon, you're currently using doesn't get disabled
            if ((event.target.id != conditional_id) && (conditional_id != "Website") && (conditional_id != "Reset"))
            {
                //Note Makes button unclickable
                $(`#${button_id}`).prop("disabled", true);

                //Note Changes tooltiptext to disabled
                $(`#${tooltip_id}`).text("Disabled")
                
                //Note Changes icon color to red
                $(`#${icon_id}`).css("color", "red")
            }
            
        }   
    }
}



export {disabled_dropdown}
