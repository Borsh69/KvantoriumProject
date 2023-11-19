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


function pointsChange(id){
  const csrftoken = getCSRFToken();
  const id_point = id.toString() + "_point";
  const id_name = id.toString() + "_name";
  const id_email = id.toString() + "_email";
  const id_login = id.toString() + "_login";
  const id_pass = id.toString() + "_pass"; 
  let emailField = document.getElementById(id_email);
  let loginField = document.getElementById(id_login);
  let nameField = document.getElementById(id_name);
  let passField = document.getElementById(id_pass);
  let pointField = document.getElementById(id_point);

  $.ajax({
    type: "POST",
    url: "/points_change/",
    data: {
      'student_id': id,
      'points': pointField.value,
      'name': nameField.value,
      'email': emailField.value,
      'login': loginField.value,
      'password': passField.value

    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    success: function(data) {
      console.log(data);
    }
  });
}