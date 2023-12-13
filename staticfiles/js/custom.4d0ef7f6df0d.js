// PASSWORD VALIDATOR

confirmPassword = document.getElementById('confirmpassword')
passwordValidator = document.getElementById('Password_Validator')
Password = document.getElementById('password')
confirmPassword.addEventListener('input', function(event){

    if (confirmPassword.value == Password.value){
        passwordValidator.innerText = 'Both passwords match'
        passwordValidator.style.color = 'green'
    }else{
        passwordValidator.style.display = 'block'
        passwordValidator.innerText = "Passwords don't match"
        passwordValidator.style.color = 'red'
    }
})

