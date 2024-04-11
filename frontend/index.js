function submit() {
    //Retriecing the values entered by the user
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var role = document.querySelector('input[name="role"]:checked').value;
    console.log(role);

    //Sending the values to the backend
    var xhr = new XMLHttpRequest();
    xhr.open('POST','http://127.0.0.1:5000/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if(xhr.readyState == XMLHttpRequest.DONE){
            if(xhr.status == 200){
                // console.log(xhr.responseText);
                //login successful, redirect user based on role
                var response = JSON.parse(xhr.responseText);
                if (role == 'admin'){
                    window.location.href = 'admin_index.html';
                }else if (role == 'professor'){
                    window.location.href = 'professor_index.html';
                }
            }else {
                //login failed
                alert('Login Failed');
            }
        }
    };
    var data = JSON.stringify({username: username, password: password, role: role});
    xhr.send(data);
}


document.getElementById('login').addEventListener('click', function(e) {
    e.preventDefault();
    submit();
})
