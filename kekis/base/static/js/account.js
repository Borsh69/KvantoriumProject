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
  let elements = document.querySelectorAll('.account-info');
  let elements2 = document.querySelectorAll('.account-projects');
  
  for (let elm of elements) {
    observer.observe(elm);
  }
  for (let elm2 of elements2) {
    observer.observe(elm2);
  }
  let popup = document.getElementById('popup'),
  popupToggle = document.getElementById('pppBtn'),
  popupClose = document.querySelector('.close');
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



  function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
  }
    
  function MyClick(index) {
    console.log(index);
  
    const catid = index;
    const csrftoken = getCSRFToken();
    
    let block = document.getElementById("like_button" + index);
    
    console.log(block);
  
     if (block.classList.contains("main-block__button")) {
      block.classList.add("main-block__button__liked");
      block.classList.remove("main-block__button");
  
      $.ajax({
              type: "POST",
              url: "/liked/",
              data: {
                  'liked_id': index
              },
              beforeSend: function(xhr) {
                  xhr.setRequestHeader('X-CSRFToken', csrftoken);
              },
              success: function(data) {
                  console.log(data);
              }
      });
    } else {
      block.classList.add("main-block__button");
      block.classList.remove("main-block__button__liked");
  
      $.ajax({
              type: "POST",
              url: "/unliked/",
              data: {
                  'liked_id': index
              },
              beforeSend: function(xhr) {
                  xhr.setRequestHeader('X-CSRFToken', csrftoken);
              },
              success: function(data) {
                  console.log(data);
              }
      });
    }
  }