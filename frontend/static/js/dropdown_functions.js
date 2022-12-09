import {check_website} from "./website_link.js"

function disabled_dropdown(event) {

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

function initilize_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    
    let standard_dropdown_dictionary = 
    {
        "Graph": split_url[3],                             //* Using the url to get the Graph Type
        "Specificity": split_url[4], 
        "Tool": split_url[5],                                    //* Using the url to get the Tool
        "ID of Dropdown": event.target.id                    //* Might Use these to fix the dropdowns later
    }
    
    if (split_url[3] == "scatter")  
    {

        if (split_url[4] == "basic")
        {

            let new_dictionary = check_ID(standard_dropdown_dictionary["ID of Dropdown"])
            let finished_dictionary = Object.assign({}, standard_dropdown_dictionary, new_dictionary);  
            
            return finished_dictionary
        }
    }
    else if (split_url[3] == "bar")
    {   

        if (split_url[4] == "count_transactions")
        {
            let new_dictionary = check_ID(standard_dropdown_dictionary["ID of Dropdown"])
            let finished_dictionary = Object.assign({}, standard_dropdown_dictionary, new_dictionary);  


            return finished_dictionary

        }
    }

    
}
function check_ID(ID){
    if ((ID == "Start-Date") || (ID == "End-Date"))
    {
        let specific_dictionary = 
        {
            "Start_Date": $("#Start-Date").val(),                    //* Using JQuery to get Start-Date value
            "End_Date": $("#End-Date").val(),                        //* Using JQuery to get End-Date value
            "Address_Type": $("#Type-Address").val()
        }
        return specific_dictionary
    }


    else if (ID == "Address"){
        let specific_dictionary = 
        {
            "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
            "Address_Type": $("#Type-Address").val()
        }
        return specific_dictionary
    }


    else if (ID == "Type-Address"){
        let specific_dictionary = 
        {
            "Address_Type": $("#Type-Address").val()               //* Using JQuery to get Type-Address value
        }
        return specific_dictionary
    }


    else if ((ID == "Less-Than") || (ID == "Greater-Than"))
    {
        let specific_dictionary = 
        {
            "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
            "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
            "Address_Type": $("#Type-Address").val()

        }
        return specific_dictionary
    }
    else if (ID == "Reset-Icon"){
        let specific_dictionary = 
        {
            "Address_Type": $("#Type-Address").val()               //* Using JQuery to get Type-Address value
        }
        return specific_dictionary
    }

}




function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    $.getJSON({
        //Note Goes to fuction update_page() because it has /calling as route
        url: "/update_page",                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 

            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
                   
            $('#badge-area').empty();


            //FIXME Need to pass in a new "Address" dropdown for when "Seller" is picked. Might have to use repopulate_address_dropdown()
            //FIXME Reset needs to clear the checkmark in the "Address" dropdpown
            $("#Address option").remove();

            console.table(result["Address List"])
            //Note Check if the key "Chosen_Addresses" is in dropdown_dictionary
            if (("Chosen_Addresses" in dropdown_dictionary))
            {
                console.log("if")
                dropdown_dictionary["Chosen_Addresses"].split(',');
                repopulate_address_dropdown(result["Address List"], selected_addresses)
                
            }
            else
            {
                console.log("else")
                for(let i = 0; i < result["Address List"].length; i++) 
                {
                    $("#Address").append($("<option>").val(result["Address List"][i]).text(result["Address List"][i]));        
                }
                

            }
            $(".selectpicker").selectpicker("refresh");
            disabled_dropdown(event);
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


export {initilize_dictionary, update_graph_and_dropdowns}
