import axios from "axios";
import Cookies from "js-cookie";

// Django default port is 8000
const currentProtocol = window.location.protocol;
const currentHost = window.location.hostname.includes("localhost")
  ? window.location.hostname + ":8000"
  : window.location.hostname;
const uri = "/api/";
const url = currentProtocol + "//" + currentHost + uri;

const axiosInstance = axios.create({
  headers: {
    accept: "application/json",
    "X-CSRFTOKEN": Cookies.get("csrftoken"),
    "Content-Type": "application/json",
  },

  xsrfHeaderName: "X-CSRFTOKEN",
  xsrfCookieName: "csrftoken",
  baseURL: url,
  timeout: 15000,
});

export default axiosInstance;
