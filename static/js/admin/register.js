// alert("Js is connected Bro...")
    const submitbtn = document.getElementById('SubmitRegister');
    const genotpbtn = document.getElementById('GenOTP')
    const buttons = document.querySelectorAll('button');
    const OtpGenerationStep = document.getElementById("OtpGenerationStep")
    const OtpVerificationStep = document.getElementById("OtpVerificationStep")
    const SubmitDetails = document.getElementById("SubmitDetails")
    OtpVerificationStep.classList.add("hidden")
    SubmitDetails.classList.add("hidden")
    window.onload = function () {


      submitbtn.classList.add("hidden")
      fetch("/register/verification")
        .then(ers => ers.json())
        .then(server => {
          window.alert("Fetched")
        })
    }


    buttons.forEach(button => {
      button.addEventListener('click', async (event) => {
        try {

          const response = await fetch('/ping');
          if (!response.ok) throw new Error('Ping failed');
          const data = await response.json();


          const clickedButtonId = event.target.id;



        } catch (error) {
          alert('Server is down. Please try again after some time');
        }
      });
    });

    genotpbtn.addEventListener('click', generate => {
      generate.preventDefault()
      alert("Please wait!! Attempting to send mail.")
      const name = document.getElementById('NameBox').value;
      const email = document.getElementById('EmailBox').value;
      const request_type = "GenerateOtp"
      const register_pack = {
        name: name,
        email: email,
        request_type: request_type
      }
      fetch('/register', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        }, body: JSON.stringify(register_pack)
      })
        .then(res => res.json()).then(server => {
          {
            alert(server.message)
          }
        })
    })

    submitbtn.addEventListener("click", e => {
      e.preventDefault()
      const username = document.getElementById("UsernameBox").value;
      const password = document.getElementById("PasswordBox").value;
      const token = document.getElementById("TokenBox").value;
      const otp = document.getElementById("OtpBox").value
      const request_type = "SubmitDetails";
      const register_pack = {
        username: username,
        password: password,
        token: token,
        otp: otp,
        request_type: request_type
      }
      fetch('/register', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        }, body: JSON.stringify(register_pack)
      }).then(res => res.json()).then(server => {

        if (server.status === "dbsuccess") {
          window.location.href = "/register/success"
        }
        else {
          alert(server.message);

        }
      })
    })

