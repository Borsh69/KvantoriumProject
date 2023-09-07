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
  