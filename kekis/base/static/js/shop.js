function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
       change.target.classList.add('element-show');
      }
    });
  }
  
  let options = {
    threshold: [0] };
  let observer = new IntersectionObserver(onEntry, options);
  let elements = document.querySelectorAll('.shop__block');
  
  for (let elm of elements) {
    observer.observe(elm);
  }
  
  function sortList() {
    var list, i, switching, b, shouldSwitch;
    list = document.getElementById("id01");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      b = list.getElementsByTagName("div");
      //Loop through all list-items:
      for (i = 0; i < (b.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*check if the next item should
        switch place with the current item:*/
        if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
          /*if next item is alphabetically
          lower than current item, mark as a switch
          and break the loop:*/
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark the switch as done:*/
        b[i].parentNode.insertBefore(b[i + 1], b[i]);
        switching = true;
      }
    }
  }
  function sortListY() {
    var list, i, switching, b, shouldSwitch;
    list = document.getElementById("id01");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      b = list.getElementsByTagName("div");
      //Loop through all list-items:
      for (i = 0; i < (b.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*check if the next item should
        switch place with the current item:*/
        if (b[i].innerHTML.toLowerCase() < b[i + 1].innerHTML.toLowerCase()) {
          /*if next item is alphabetically
          lower than current item, mark as a switch
          and break the loop:*/
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark the switch as done:*/
        b[i].parentNode.insertBefore(b[i + 1], b[i]);
        switching = true;
      }
    }
  }
  
  let 
  search = document.getElementById('search'),
  search_button = document.getElementById('search_button'),
  search_body = document.getElementById('search_body'),
  search_field = document.getElementById('search_field'),
  search_submit = document.getElementById('search_submit'),
  search_popup = document.getElementById('search_popup')
  
search_button.onclick = function() {
  search_button.style.transform = "rotate(90deg)";
  search_body.style.opacity = '1';
  search_body.style.visibility = 'visible'
  search.style.left = '-285px'
  search_popup.style.display = 'block'
  }
  
  window.onclick = function(e){
    if(e.target == search_popup){
      search_button.style.transform = "rotate(0deg)";
      search_body.style.opacity = '0';
      search_body.style.visibility = 'hidden'
      search.style.left = '0'
      search_popup.style.display = 'none'
    }
  }
