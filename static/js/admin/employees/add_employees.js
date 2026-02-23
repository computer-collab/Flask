// alert("Hello World");

//JS STARTS HERE
const  MessageBox = document.getElementById("message");
const NameBox = document.getElementById("NameBox");
const EmailBox = document.getElementById("EmailBox");
const WorkerTypeBox = document.querySelectorAll(".radio-label");
const ProfilePicInput = document.getElementById("ProfilePicInput");
const ProfilePic = document.getElementById("ProfilePic");
const Preview=document.getElementById("Preview");
const PreviewBackground = document.getElementById("PreviewBackground");

const PreviewButton=document.getElementById("PreviewButton");


let  StoredPhoto = null;




WorkerTypeBox.forEach(click =>{
    click.addEventListener("click",()=>{
        alert("button is clicked")
    })
})
ProfilePic.addEventListener("click", () => {
    ProfilePicInput.click();
});

ProfilePicInput.addEventListener("change", () => {

  const file = ProfilePicInput.files[0];

  if (!file) return;

  preview.src = URL.createObjectURL(file);

});
PreviewButton.addEventListener('click',(Button)=>{
PreviewButton.addEventListener('click', () => {
    if (PreviewBackground.style.display === "block") {
        PreviewBackground.style.display = "none";
    } else {
        PreviewBackground.style.display = "block";
    }
});})







let storedPhoto = null;

const input = document.getElementById("ProfilePicInput");
const preview = document.getElementById("Preview");

input.addEventListener("change", function(){

    storedPhoto = input.files[0];

    const reader = new FileReader();

    reader.onload = function(e){

        preview.src = e.target.result;

    }

    reader.readAsDataURL(storedPhoto);

});