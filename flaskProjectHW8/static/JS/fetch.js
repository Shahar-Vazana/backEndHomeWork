console.log('inside fetch JS file');

function myFunction() {
    console.log('clicked')
    fetch('https://reqres.in/api/users?page=2').then(
        response => response.json() //להמיר לג'ייסון טהור
    ).then(
        // response_obj => console.log(response_obj)
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        error => console.log(error)
    )
}

function put_users_inside_html(response_obj){
    const currMain = document.querySelector(selectors:"main");
    for (let user of response_obj){
        const section = document.createElement(tagName:'section');
        section.innerHTML= `
            <img src="${user.avatar}" alt="profile pic"/>
            <div>
                <span> ${user.first_name} ${user.last_name}</span> <br>
                <a href="mailto:${user.email}"> Send Email </a>
            </div>
            `;
    }
}

