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

function question_mark_ping(id)
{
  let selected_less_than = $('#Less-Than option:selected').val();
  let selected_greater_than = $('#Greater-Than option:selected').val();
  let selected_start_date = $('#Start-Date').val();
  let selected_end_date = $('#End-Date').val();

  if (id != "Reset-Icon")
  {
    if ((selected_less_than < selected_greater_than) || (selected_greater_than > selected_less_than))
    {

      $("#Question").show()
    }

    else if ((selected_start_date > selected_end_date) || (selected_end_date < selected_start_date))
    {
      $("#Question").show()
    }
  }
}
export {reveal_dropdown, question_mark_ping}