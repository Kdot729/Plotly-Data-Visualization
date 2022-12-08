import {trigger_date_dropdown, initilize_dictionary, update_graph_and_dropdowns} from "./dropdown_functions.js"
import {check_website} from "./website_link.js"

let string_url = window.location.href
let split_url = string_url.split("/")


// let id_dictionary = $(".custom-tooltip").children("button[id$='Button']")
//Note Select all "button" tag where the parent has a class "custom-tooltip"
let button_id_list = $.map($('.custom-tooltip > button'), button_id => button_id.id);
console.log(button_id_list)

//Note Select all "span" tag where the parent has a class "custom-tooltip"
let tooltip_id_list = $.map($('.custom-tooltip > span'), span_id => span_id.id);
console.log(tooltip_id_list)

//Note Select all "i" tag where the parent is a "button" tag
let icon_id_list = $.map($('button > i'), i_id => i_id.id);
console.log(icon_id_list)


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
  
      //Note Example of dropdown_substring
      //Note End-Than-Dropdown
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

    $("#Address-Type").on("change", function(event)
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




    });
    

function update_page(event)
{
    let dropdown_dictionary = initilize_dictionary(event);
    update_graph_and_dropdowns(dropdown_dictionary, event);
};

    




//! Maybe get rid of the reset button
// $(document).ready(function () { 
//     $('#Reset').on("click", function(event){
//         let graph = update_graph(undefined, event);
//         console.log(graph)
//         let graph2 = update_dropdown(undefined, event);
//         console.log(graph2)
    
//         });
//     })

