import {check_website} from "./website_link.js"

function trigger_date_dropdown(event) {

    if ((event.target.id != "Start-Date") && (event.target.id != "End-Date") && (event.target.id != "Address-Type"))
    { 
        disable_dropdown("True")
    }
    
    if (event.target.id == "Address-Type")
    { 
        disable_dropdown("False")
    }

    if(($("#Address").val().length == 0) && ($("#Less-Than").val() == "") && ($("#Greater-Than").val() == ""))
    {
        disable_dropdown("False")
    }
}

function disable_dropdown(date_boolean){
    if (date_boolean == "True"){

        //Note Make it so both date dropdown aren't clickable
        $("#Start-Date-Icon-Button").prop("disabled", true);
        $("#End-Date-Icon-Button").prop("disabled", true);

        $("#Start-Date-Icon").css("color", "red");
        $("#End-Date-Icon").css("color", "red");
        $("#Start-Date-Tooltip").text("Disabled")
        $("#End-Date-Tooltip").text("Disabled")
    }
    else if (date_boolean == "False"){

        //Note Make it so both date dropdown are clickable again
        $("#Start-Date-Icon-Button").prop("disabled", false);
        $("#End-Date-Icon-Button").prop("disabled", false);

        $("#Start-Date-Icon").css("color", "#004489");
        $("#End-Date-Icon").css("color", "#004489");
        $("#Start-Date-Tooltip").text("Start Date")
        $("#End-Date-Tooltip").text("End Date")
    }

}
function initilize_dictionary(event)
{
    let string_url = window.location.href
    let split_url = string_url.split("/")
    
    let standard_dropdown_dictionary = 
    {
        // "Start_Date": $("#Start-Date").val(),                    //* Using JQuery to get Start-Date value
        // "End_Date": $("#End-Date").val(),                        //* Using JQuery to get End-Date value
        // "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
        // "Address_Type": $("#Address-Type").val(),               //* Using JQuery to get Address-Type value
        // "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
        // "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
        "Graph": split_url[3],                             //* Using the url to get the Graph Type
        "Specificity": split_url[4], 
        "Tool": split_url[5],                                    //* Using the url to get the Tool
        "ID of Dropdown": event.target.id                    //* Might Use these to fix the dropdowns later
    }

    if (split_url[3] == "scatter")  
    {
        console.log('1')
        if (split_url[4] == "basic")
        {
            let new_dictionary =
            {
                "Start_Date": $("#Start-Date").val(),                    //* Using JQuery to get Start-Date value
                "End_Date": $("#End-Date").val(),                        //* Using JQuery to get End-Date value
                "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
                "Address_Type": $("#Address-Type").val(),               //* Using JQuery to get Address-Type value
                "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
                "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
            }
            let finished_dictionary = Object.assign({}, standard_dropdown_dictionary, new_dictionary);  
            console.table(finished_dictionary)
            return finished_dictionary
        }
    }
    else if (split_url[3] == "bar")
    {   
        console.log('2')
        if (split_url[4] == "count_transactions")
        {
            let new_dictionary =
            {
            "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
            "Address_Type": $("#Address-Type").val(),               //* Using JQuery to get Address-Type value
            "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
            "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
            }
            let finished_dictionary = Object.assign({}, standard_dropdown_dictionary, new_dictionary);  
            console.table(finished_dictionary)
            return finished_dictionary

        }
    }

    
}

// function initilize_dictionary(event)
// {
//     let string_url = window.location.href
//     let split_url = string_url.split("/")
    
//     let dropdown_dictionary = 
//     {
//         "Start_Date": $("#Start-Date").val(),                    //* Using JQuery to get Start-Date value
//         "End_Date": $("#End-Date").val(),                        //* Using JQuery to get End-Date value
//         "Chosen_Addresses": ($("#Address").val()).toString(),  //* Using JQuery to get Address value, then converting to string
//         "Address_Type": $("#Address-Type").val(),               //* Using JQuery to get Address-Type value
//         "Less_Than": $("select#Less-Than").val(),               //* Using JQuery to get Less-Than selected value
//         "Greater_Than": $("select#Greater-Than").val(),          //* Using JQuery to get Greater-Than selected value
//         "Graph": split_url[3],                             //* Using the url to get the Graph Type
//         "Specificity": split_url[4], 
//         "Tool": split_url[5],                                    //* Using the url to get the Tool
//         "ID of Dropdown": event.target.id                    //* Might Use these to fix the dropdowns later
//     }

//     return dropdown_dictionary
// }



function update_graph_and_dropdowns(dropdown_dictionary, event) 
    {
    $.getJSON(
        {

        //Note Goes to fuction update_page() because it has /calling as route
        url: "/update_page",                                   
        data: dropdown_dictionary,
        success: function (result) 
        { 

            //Note JSON.parse(result["JSON Graph"]) converts data into a object. Need to have it as an object
            Plotly.newPlot("chart", JSON.parse(result["JSON Graph"]), {staticPlot: true});
            
            //Note Includes the "badge-area"
            empty_dropdowns();

            //Note This is necessary becuase if don't put an empty string in, it will ruin the query when selecting multiple address
            //Note Make sure .val() is empty or it will ruin the query of DataFrame, too, when selecting multiple address
            //Note Changing .val() will also mess with a condition in trigger_date_dropdown()
            if ((event.target.id != "Less-Than") && (event.target.id != "Greater-Than"))
            {        
                $("#Less-Than").append($("<option>").val("").text("None"));
                $("#Greater-Than").append($("<option>").val("").text("None"));
            }

            //! This is causing problem when using "reset" becuase the dictionary is empty
            let selected_address = dropdown_dictionary["Chosen_Addresses"].split(","); 

            repopulate_inequality_dropdowns("Less-Than", result["Descending List"]);
            repopulate_inequality_dropdowns("Greater-Than", result["Ascending List"]);
            repopulate_address_dropdown(result["Address List"], selected_address); 
            
            
            if (result["Link Address"] !== null)
            {
                check_website($("#Website").val(), result["Link Address"]);

            
            }
            
            $(".selectpicker").selectpicker("refresh"); 

            trigger_date_dropdown(event);


        }
        })
    };
function empty_dropdowns()
{   
    $('#badge-area').empty();
    $("#Less-Than").empty();
    $("#Greater-Than").empty();

    //! Forget what this does, but "Address" dropdown works. I think it removes all the options
    $("#Address option").remove();
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


export {trigger_date_dropdown, initilize_dictionary, update_graph_and_dropdowns}