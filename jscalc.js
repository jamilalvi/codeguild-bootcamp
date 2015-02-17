function calculate(evt) {
   var result;
   var frm = document.getElementById('calcform');
   
   switch(evt.target.name) {
      case 'addbutton':
         result = parseFloat(frm.input_a.value) + parseFloat(frm.input_b.value);
         break;
         
      case 'subbutton':
         result = parseFloat(frm.input_a.value) - parseFloat(frm.input_b.value);
         break;         
   }
      
   document.getElementById("result").textContent = result;
}

// This event called when the DOM is fully loaded and parsed 
document.addEventListener("DOMContentLoaded", function (event) {

   // Get the FORM 
   var frm = document.getElementById('calcform');

   // Attach an event handler for the click event 
   frm.addbutton.onclick = calculate;
   frm.subbutton.onclick = calculate;
});

