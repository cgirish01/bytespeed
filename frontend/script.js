document.getElementById('contact-form').addEventListener('submit', function (event) {
    event.preventDefault();
    let email = document.getElementById('email').value;
    let phoneNumber = document.getElementById('phoneNumber').value;
    let data = {
        email: email,
        phoneNumber: phoneNumber
    };
    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };
    fetch('/api/identify/', options)
        .then(response => response.json())
        .then(data => document.getElementById('result').textContent = JSON.stringify(data, null, 2))
        .catch(error => console.error('Error:', error)); // Added .catch block here
});


