function reveal_dropdown(event)
{

          let split_event = event.target.id.split("-")  

    
          //Note Minus two because we don't need the "style-icon" part
          let partial_id = "";
          for (let i = 0; i < split_event.length-1; i++) 
          {
            partial_id += split_event[i] + "-";
          }
      
          //Note Example of dropdown_substring, "End-Than-Dropdown"
          let dropdown_id = partial_id + "Dropdown"

          if ($(`#${dropdown_id}`).is(":visible") == false)
          {   
            $(`#${dropdown_id}`).show()       
          }
          // else if ($(`#${dropdown_id}`).is(":visible") == true )
          // {  
          //   $(`#${dropdown_id}`).hide()    
          // }
}

export {reveal_dropdown}