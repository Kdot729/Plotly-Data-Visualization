import {initilize_dictionary} from "../bar/dictionary.js"
import {update_graph_and_dropdowns} from "../bar/update.js"
import {button_click} from "../button_click.js"
import {changed_website} from "../link.js"



//TODO "Reset-Icon" triggers this function. Not sure if that's going to be a problem later
$(document).ready(function () {

    //Note Selector is all button tags that end with "Button". It's case sensitive
    //Example id that is called "Address-Icon-Button"
    $("button[id$='Button']").on("click", function(event) 
    {
      button_click(event)
    });
  
  
    $(document).on("click", function(event) 
    {
      //FIX Put "content" in all the dropdown to make it easier to hide. Need to replace "content" later
      $(".custom-tooltip").not($(".custom-tooltip").has($(event.target))).children(".content").hide()
  
    })

    $("#Address").on("change", function(event)
    {
      update_page(event);

    });

    $("#Transaction-Type").on("change", function(event)
    {   
      update_page(event);
        
    });

    $("#Less-Than").on("change", function(event)
    {
      update_page(event);
    });


    $("#Greater-Than").on("change", function(event)
    {
      update_page(event);
    });



    $("#Website").on("change", function()
    {
      changed_website();
    });

    $('#Reset-Icon').on("click", function(event)
    {
      update_page(event);
    
    })


    });
    

function update_page(event)
{
    let dropdown_dictionary = initilize_dictionary(event);
    update_graph_and_dropdowns(dropdown_dictionary, event);
};
