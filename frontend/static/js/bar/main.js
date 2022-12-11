import {initilize_dictionary} from "../bar/dictionary.js"
import {update_graph_and_dropdowns} from "../bar/update.js"
import {button_click} from "../button_click.js"



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



    $("#Website").on("change", function(event)
    {
      //Note This is neccesary because without it will include Zapper website and the new website, essentiatly doubling the actually amount of badges need
      //Note We only need the badges from the new website so .empty() is neccesary in this function too because we never call update_page which has $('#badge-area').empty()
      $("#badge-area").empty();

      if ($("#Website").val() == "Blur")
          alert("Blur requires you to connect a wallet to use. If you're not comfortable with that they use the other sites");
      if (($("#Address").val()).length != 0)
          check_website($("#Website").val(), $("#Address").val())
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
