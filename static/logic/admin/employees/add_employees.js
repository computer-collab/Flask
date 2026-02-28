// alert("Hello World");

//JS STARTS HERE
const MessageBox = document.getElementById("message");
const NameBox = document.getElementById("NameBox");
const EmailBox = document.getElementById("EmailBox");
const WorkerTypeBox = document.getElementById("WorkerType");
const FORM = document.querySelector("form");
const ProfilePicInput = document.getElementById("ProfilePicInput");
const ProfilePic = document.getElementById("ProfilePic");

const Preview = document.getElementById("Preview");

const PreviewForeground = document.getElementById("PreviewForeground");
const PreviewBackground = document.getElementById("PreviewBackground");
const PreviewButton = document.getElementById("PreviewPicButton");
function clicked (){ alert("The element was clicked")}
let tempPhoto = null;//Used to temporarily copy the photo
let StoredPhoto = null;// Used to store the actual photo


// Temporary profile pic storage and preview
ProfilePicInput.addEventListener("change",(x)=>{
    tempPhoto = ProfilePicInput.files[0];
    if(tempPhoto){
        StoredPhoto = tempPhoto;    
    }
    
    const reader = new FileReader();
    reader.onload =  (ed)=>{
        Preview.src = ed.target.result;
    }
    reader.readAsDataURL (StoredPhoto)
})


PreviewBackground.addEventListener("click",()=>{
    
    if (PreviewBackground.hidden == false || PreviewBackground.style.display != "none"){
        PreviewBackground.style.display="none";
    }
})
ProfilePic.addEventListener("click", () => {
    ProfilePicInput.click();
});


PreviewButton.addEventListener('click', () => {
    if(PreviewBackground.hidden == true || PreviewBackground.style.display == "none"){
        if (!StoredPhoto.type.startsWith("image/") || StoredPhoto==null ){
            alert("Empty Photo");
        }else {
             PreviewBackground.hidden = false
        PreviewBackground.style.display = "flex"
        
        }
    } else {
        clicked();
        console.log(PreviewBackground.style.display , PreviewBackground.hidden)
    }
})


WorkerTypeBox.
    addEventListener("change", () => {
        if (WorkerTypeBox.value === "others") {
            inputobj = document.getElementById("OthershelperDiv");
            inputbtn = document.getElementById("othersbutton");
            inputobj.hidden = false;
            
        
        }else {
                document.getElementById("OthershelperDiv").hidden = true
            }})


document.getElementById("submitbutton").addEventListener("click",Submit=>{
    Submit.preventDefault()
    if (!StoredPhoto){
        alert("empty photo")
        return
    }
        FORM.requestSubmit()
})