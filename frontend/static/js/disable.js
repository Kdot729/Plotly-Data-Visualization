import {check_website} from "./badges.js"


function disabled_icon(event) 
{
    //Note Select all "span" tag where the parent has a class "custom-tooltip"
    let tooltip_id_list = $.map($('.custom-tooltip > span'), span_id => span_id.id);

    // console.log("before condition",event.target.id)
    if (event.target.id == "Reset-Icon")
    {
        reset_icon_clicked(tooltip_id_list, event)
    }
    
    //Note "Type" won't disable other icons
    else if ((event.target.id != "Reset-Icon") && (event.target.id != "Type"))
    {
        other_icons_clicked(tooltip_id_list, event)
    }
}

function reset_icon_clicked(tooltip_id_list){
    for(let i = 0; i < tooltip_id_list.length; i++)
    {
        let split_id = tooltip_id_list[i].split("Tooltip")[0]

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

function other_icons_clicked(tooltip_id_list, event){
       
    //Note Split the event by "-" then grab the last index
    let last_index_event_id = (event.target.id.split("-")).at(-1)


    //Note Iterate through all the icons
    //Note Passing tooltip id because it's the easiest to split
    for(let i = 0; i < tooltip_id_list.length; i++)
        {

            //Example of split_id: Start-Date-
            let split_id = tooltip_id_list[i].split("Tooltip")[0]
            
            //Example of button_id: Start-Date-Icon-Button
            let button_id = split_id + "Icon-Button"

            //Example of tooltip_id: Start-Date-Tooltip
            let tooltip_id = split_id + "Tooltip"

            //Example of icon_id: Start-Date-Icon
            let icon_id = split_id + "Icon"

            
            //Note Get get of last character which is "-" because event.target.id doesn't have a "-" 
            //Example of id: Start-Date
            let id = split_id.slice(0, -1)

            //Note Split all the ids by "-" then grab the last index
            //Example of last_index_id: It would split "Start-Date" in a list containing "Start" and "Date" then grab the last index which is "Date"
            let last_index_id = (id.split("-")).at(-1)


            //Note Harded coding that the "Website" and "Reset" icon don't get disabled
            //Note (event.target.id != id) makes it so the icon, you're currently using doesn't get disabled
            //Note (last_index_event_id != last_index_id) makes it so icon that are the same don't get disabled
            //Example If "Start-Date" or "End-Date" gets used the other date icon doesn't get disabled
            //Example If "Less-Than" or "Greater-Than" gets used the other inequality icon doesn't get disabled
            if ((event.target.id != id) && (id != "Website") && (id != "Reset") && (last_index_event_id != last_index_id))
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
export {disabled_icon}
