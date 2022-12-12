import {initilize_dictionary} from "../bar/dictionary.js"
import {update_graph_and_dropdowns} from "../bar/update.js"
import {reveal_dropdown} from "../reveal.js"
import {changed_website} from "../badges.js"




$(document).ready(function () {

    //Note Selector is all button tags that end with "Button". It's case sensitive
    //Example id that is called "Address-Icon-Button"
    $("button[id$='Button']").on("click", function(event) 
    {
      //Note Don't need to show dropdown for "Reset-Icon" because there's no dropdown for the "reset"
      if (event.target.id != "Reset-Icon")
        {reveal_dropdown(event)}
    });
  
  
    $(document).on("click", function(event) 
    {
      $(".custom-tooltip").not($(".custom-tooltip").has($(event.target))).children(".reveal").hide()
  
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
