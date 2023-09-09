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
  let elements = document.querySelectorAll('.main_block');
  
  for (let elm of elements) {
    observer.observe(elm);
  }
let popup = document.getElementById('popup'),
  popupToggle = document.getElementById('pppBtn'),
  popupClose = document.querySelector('.close');

popupToggle.onclick = function(){
    popup.style.display = "block";
    popup.style.opacity = "1";
  };

  popupClose.onclick = function(){
    popup.style.display = "none";
    popup.style.opacity = "0";
  }

  window.onclick = function(e){
    if(e.target == popup){
      popup.style.display = "none";
      popup.style.opacity = "0";
    }
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

$(document).ready(function() {
    $(document).on('click', '.main-block__button', function() {
        console.log('click');
    });
});
/*
$(document).on('click', '.main-block__button', function() {
    $(this).addClass("main-block__button__liked").removeClass("main-block__button");
    const catid = $(this).attr("data-catid");
    const csrftoken = getCSRFToken();

    $.ajax({
        type: "POST",
        url: "/liked/",
        data: {
            'liked_id': catid
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
            console.log(data);
        }
    });
});


$(document).on('click', '.main-block__button__liked', function() {
    $(this).addClass("main-block__button").removeClass("main-block__button__liked");
    const catid = $(this).attr("data-catid");
    const csrftoken = getCSRFToken();

    $.ajax({
        type: "POST",
        url: "/unliked/",
        data: {
            'liked_id': catid
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
        }
    });
});

*/