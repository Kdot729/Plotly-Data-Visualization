import {initilize_dictionary} from "./dictionary.js"
import {update_graph_and_dropdowns} from "./update.js"
import {reveal_dropdown} from "../reveal.js"
import {changed_website} from "../link.js"


//TODO "Reset-Icon" triggers this function. Not sure if that's going to be a problem later
$(document).ready(function () {

    //Note Selector is all button tags that end with "Button". It's case sensitive
    //Example id that is called "Address-Icon-Button"
    $("button[id$='Button']").on("click", function(event) 
    {
      reveal_dropdown(event)
    });
  
  
    $(document).on("click", function(event) 
    {
      //! Put "content" in all the dropdown to make it easier to hide. Need to replace "content" later
      $(".custom-tooltip").not($(".custom-tooltip").has($(event.target))).children(".content").hide()
  
    })

    $("#Start-Date").on("change", function(event)
    {
      update_page(event);     
    });

    $("#End-Date").on("change", function(event)
    {
      update_page(event);
    });

    $("#Address").on("change", function(event)
    {
      update_page(event);

    });

    $("#Type").on("change", function(event)
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
      changed_website()
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
