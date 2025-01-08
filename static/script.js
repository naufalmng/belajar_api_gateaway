// Dockerfile/script.js
document.getElementById('fetchUserBtn').addEventListener('click', function() {
  fetch('103.31.39.20:7000/api/users')
    .then(response => response.json())
    .then(data => {
      console.log(data.data);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});
document.getElementById('addUserBtn').addEventListener('click', function() {
    const form = document.getElementById('userForm');
    const formData = new FormData(form)
    const data = Object.fromEntries(formData.entries())
    fetch('103.31.39.20:7000/api/users', {
      method: "POST",
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({data})
  })
    .then(response => response.json())
    .then(json => {
      console.log(json);
    })
    .catch(error => {
      console.error('Error adding data:', error);
    });
});


