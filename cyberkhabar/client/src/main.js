import { createApp } from "vue";
import App from "./App.vue";
import "./style.css";
import axios from "axios";

createApp(App).mount("#app");

axios
  .get("http://localhost:3001/api/data")
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error(error);
  });
