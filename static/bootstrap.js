
class LoginPanel {
    constructor(){

    }
    get_user_name(){
        return $("#username").value;
    }
    get_password(){
        return $("#password").value;
    }

}

$(document).ready(() => {
    login_panel = new LoginPanel()
    $(".login").click(() => {
        const username = login_panel.get_user_name();
        const password = login_panel.get_password();

        $.post(
            "/authenticate", 
            {'username': username, 'password': password},
            (data) => {console.log(data)},
            "json"
        )
        
    })
    

})