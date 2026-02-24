// alert("Hello World");

//JS STARTS HERE
const MessageBox = document.getElementById("message");
const NameBox = document.getElementById("NameBox");
const EmailBox = document.getElementById("EmailBox");
const WorkerTypeBox = document.getElementById("WorkerType");
const ProfilePicInput = document.getElementById("ProfilePicInput");
const ProfilePic = document.getElementById("ProfilePic");

const Preview = document.getElementById("Preview");

const PreviewForeground = document.getElementById("PreviewForeground");
const PreviewBackground = document.getElementById("PreviewBackground");
const PreviewButton = document.getElementById("PreviewPicButton");
function clicked (){ alert("The element was clicked")}

let StoredPhoto = null;




WorkerTypeBox.
    addEventListener("change", () => {
        if (WorkerTypeBox.value === "others") {
            inputobj = document.getElementById("OthershelperDiv");
            inputbtn = document.getElementById("othersbutton");
            inputobj.hidden = false;
            
        
        }else {
                document.getElementById("OthershelperDiv").hidden = true
            }})


PreviewBackground.addEventListener("click",()=>{
    
    if (PreviewBackground.hidden == false || PreviewBackground.style.display != "none"){
        PreviewBackground.style.display="none";
    }
})
ProfilePic.addEventListener("click", () => {
    ProfilePicInput.click();
});

ProfilePicInput.addEventListener("change", () => {
    const file = ProfilePicInput.files[0];
    if (!file) return;
    preview.src = URL.createObjectURL(file);
});
PreviewButton.addEventListener('click', () => {
    if(PreviewBackground.hidden == true || PreviewBackground.style.display == "none"){
        PreviewBackground.hidden = false
        PreviewBackground.style.display = "block"
    } else {
        clicked();
        console.log(PreviewBackground.style.display , PreviewBackground.hidden)
    }
})







let storedPhoto = null;

const input = document.getElementById("ProfilePicInput");
const preview = document.getElementById("Preview");

input.addEventListener("change", function () {

    storedPhoto = input.files[0];

    const reader = new FileReader();

    reader.onload = function (e) {

        preview.src = e.target.result;

    }

    reader.readAsDataURL(storedPhoto);

});