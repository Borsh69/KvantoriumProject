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
  search = document.getElementById('search'),
  search_button = document.getElementById('search_button'),
  search_body = document.getElementById('search_body'),
  search_field = document.getElementById('search_field'),
  search_submit = document.getElementById('search_submit'),
  search_popup = document.getElementById('search_popup')
  
search_button.onclick = function(){
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

 