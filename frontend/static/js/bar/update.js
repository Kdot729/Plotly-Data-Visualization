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