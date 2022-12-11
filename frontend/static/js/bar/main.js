import {initilize_dictionary} from "../bar/dictionary.js"
import {update_graph_and_dropdowns} from "../bar/update.js"
// import {check_website} from "../link"
// import {disabled_icon} from "../disable"

console.log("wtf")
//TODO "Reset-Icon" triggers this function. Not sure if that's going to be a problem later
$(document).ready(function () {

    //Note Selector is all button tags that end with "Button". It's case sensitive
    //Example id that is called "Address-Icon-Button"
    $("button[id$='Button']").on("click", function(event) 
    {

      // console.log(event.target.id)
      let split_event = event.target.id.split("-")  
      // console.log("split ",split_event)

      //Note Minus two because we don't need the "style-icon" part
      let partial_id = "";
      for (let i = 0; i < split_event.length-1; i++) 
      {
        partial_id += split_event[i] + "-";
      }
    //   console.log("partial_id",partial_id)
  
      //Note Example of dropdown_substring, "End-Than-Dropdown"
      let dropdown_id = partial_id + "Dropdown"
    //   console.log("dropdown_id", dropdown_id)
      if ($(`#${dropdown_id}`).is(":visible") == false )
      {   
        $(`#${dropdown_id}`).show()       
      }
      else if ($(`#${dropdown_id}`).is(":visible") == true )
      {  
        $(`#${dropdown_id}`).hide()    
      }
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
