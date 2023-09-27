function sendPostRequest(data) {
  // data should be a dict
  // easly send post-requests to the back-end

  const statusElement = document.getElementById("status");
  const inputElement = document.getElementById("userInput");
  const is_commited = data["commit"];

  fetch("http://127.0.0.1:8000/api/ibans/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      if (data["is_valid"] === false) {
        if (data["errors"].length === 0) {
          statusElement.textContent = "The IBAN you entered is INVALID";
          if (is_commited) {
            inputElement.value = "";
            statusElement.textContent = "Your INVALID IBAN was stored !";
          }
        } else {
          statusElement.textContent = data["errors"][0];
        }
      } else {
        statusElement.textContent = "The IBAN you entered is VALID";
        if (is_commited) {
          inputElement.value = "";
          statusElement.textContent = "Your IBAN was validated and stored !";
        }
      }
    });
}
