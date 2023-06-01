import axios from "axios";

async function getUserIP() {
    const response = await axios.get('https://api.ipify.org?format=json');
    return response.data.ip;
}

export default {
    getUserIP,
}