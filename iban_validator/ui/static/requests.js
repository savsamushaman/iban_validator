function sendGetRequest() {
  fetch("http://127.0.0.1:8000/api/ibans/")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response data here
      console.log("GET Response:", data);
    })
    .catch((error) => {
      // Handle errors
      console.error("GET Error:", error);
    });
}

function sendPostRequest(data) {
  fetch("http://127.0.0.1:8000/api/ibans/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data), // Replace 'data' with your POST request data
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response data here
      console.log("POST Response:", data);
    })
    .catch((error) => {
      // Handle errors
      console.error("POST Error:", error);
    });
}

// Example usage:
// Send a GET request
sendGetRequest();

// Send a POST request with data
const postData = { field1: "value1", field2: "value2" };
sendPostRequest(postData);
