// document.addEventListener("DOMContentLoaded", EditEmailLabel(){
//     document.getElementById('hint_id_username').innerHTML = "Utilizzare la propria email istituzionale fornita dal L.S.S Volterra"
// });


// function EditEmailLabel() {
//   document.getElementById('hint_id_username').innerHTML = "Utilizzare la propria email istituzionale fornita dal L.S.S Volterra"
// }


var label = document.createElement('small');
label.setAttribute('class', 'form-text text-muted');
label.innerHTML = "Utilizzare la propria email istituzionale fornita dal L.S.S Volterra"

const target = document.getElementById('id_email');
target.after(label)
