import { createApp } from "vue"
import App from "./App.vue"
import { setAuthToken } from "./services/api"

const token = localStorage.getItem("access_token")
if (token) {
  setAuthToken(token)
}

createApp(App).mount("#app")
