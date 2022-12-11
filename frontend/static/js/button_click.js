function button_click(event)
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
            console.log("3")
            $(`#${dropdown_id}`).show()       
          }
          else if ($(`#${dropdown_id}`).is(":visible") == true )
          {  
            console.log("4")
            $(`#${dropdown_id}`).hide()    
          }
}

export {button_click}