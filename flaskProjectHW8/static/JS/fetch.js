console.log('inside fetch js file');


function myFunction() {
    // console.log('clicked');
    let number= document.getElementById("front_number")
    fetch('https://reqres.in/api/users/'+number.value).then(
        response => response.json()
    ).then(
        (response_obj) => {
            return put_users_inside_html(response_obj.data)
        }
    ).catch(
        error => console.log(error)
    )
}

function put_users_inside_html(response_obj) {
    const curr_main = document.querySelector("main");
        const section = document.createElement('section');
        curr_main.innerHTML = `
            <img src="${response_obj.avatar}" alt="Profile Picture"/>
            <div> 
                <span>${response_obj.name}</span>
                <br>
                <a href="mailto:${response_obj.email}">Send Email</a>
            </div>
            `;
    // curr_main.appendChild(section);


}