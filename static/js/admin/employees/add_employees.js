alert("hello world");
message=document.getElementById("message");
button = document.querySelectorAll(".radio-label")
button.forEach(R=> R.addEventListener("click", function() {
    selected = document.querySelector('input[name="employee_type"]:checked');
        document.getElementById("message").innerHTML = "You have selected " + selected.value;
        alert("You have selected " + selected.value);
    }));    

function clicked(){
    window.location.href = "/admin/employees";
}