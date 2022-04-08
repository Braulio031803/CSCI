window.addEventListener("load", function ()
{
    let counter = 0;
  
  //camelCase
  function buttonClicked()
  {
   counter++;
  
   let clickedCounterElement = document.getElementById("clickCounter"); 
  
    clickedCounterElement.innerHTML = "Clicked " + counter + " times. ";
  }
  
  let clickedButtonElement = document.getElementById("clickbutton");
  
  clickedButtonElement.addEventListener("click", buttonClicked);
});
