function reset_selected_inequality()
{
    //Note Resest the selected value of each inequality since it's the default graph we can grab the zeroth index because it's the min and max
    $('#Less-Than').prop("selectedIndex", 0);
    $('#Greater-Than').prop("selectedIndex", 0);
};

function always_empty()
{   
    $('#badge-area').empty();
    // $("#Less-Than").empty();
    // $("#Greater-Than").empty();

    //! Forget what this does, but "Address" dropdown works. I think it removes all the options from "Address"
    $("#Address option").remove();
};
function repopulate_inequality_dropdowns(selector_ID, inequality_list)
{
    for(let i = 0; i < inequality_list.length; i++)
        $(selector_ID).append($("<option>").val(inequality_list[i]).text(inequality_list[i]));
};

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

export {reset_selected_inequality,
        always_empty,
        repopulate_inequality_dropdowns,
        repopulate_address_dropdown
        }