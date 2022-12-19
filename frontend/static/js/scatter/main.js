import {initilize_dictionary} from "../dictionary.js"
import {update_graph_and_dropdowns} from "./update.js"
import {reveal_dropdown} from "../reveal.js"
import {website_changed} from "../badges.js"


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
      if ($(".reveal").is(":visible") == true)
      {
        //! Have no idea how this works, but dropdown disappears when clicking outisde and clicking on other dropdowns
        $(".custom-tooltip").not($(".custom-tooltip").has($(event.target))).children(".reveal").hide()
      }
  
    })

    //TODO Need to change ".send" to something that makes more sense 
    //Note on click too because of "Reset-Icon" doesn't have a dropdown
    $(".send").on("change", function(event)
    {
      if (event.target.id == "Website")
      {
        website_changed();
      }
      else if (event.target.id != "Website")
      {
        update_page(event);
      }
    });

    $(".send").on("click", function(event)
    {
      if (event.target.id == "Reset-Icon")
      {
        update_page(event);
      }
    });

    }); //Organization End of $(document).ready
    

function update_page(event)
{
    let dropdown_dictionary = initilize_dictionary(event);
    update_graph_and_dropdowns(dropdown_dictionary, event);
};
