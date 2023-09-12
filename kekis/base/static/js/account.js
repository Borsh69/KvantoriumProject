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
    
  $(document).ready(function() {
    $("#like_button").on("click", function() {
        const catid = $(this).attr("data-catid");
        const csrftoken = getCSRFToken();
  
        if ($(this).hasClass("main-block__button")) {
          $(this).addClass("main-block__button__liked").removeClass("main-block__button");
  
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
      } else {
          $(this).addClass("main-block__button").removeClass("main-block__button__liked");
  
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
                  console.log(data);
              }
          });
      }
    });
  });
  