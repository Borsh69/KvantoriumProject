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