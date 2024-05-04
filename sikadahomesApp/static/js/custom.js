// PASSWORD VALIDATOR

confirmPassword = document.getElementById('confirmpassword')
passwordValidator = document.getElementById('Password_Validator')
Password = document.getElementById('password')
submit_btn = document.getElementById('submit_btn')

confirmPassword.addEventListener('input', function(event){

    if (confirmPassword.value == Password.value){
        passwordValidator.innerText = 'Both passwords match'
        passwordValidator.style.color = 'green'
        submit_btn.disabled = false
        
    }else{
        passwordValidator.style.display = 'block'
        passwordValidator.innerText = "Passwords don't match"
        passwordValidator.style.color = 'red'
        submit_btn.disabled = true
    }
})

