import axios from "axios";
import VueAxios from "vue-axios";

class ApiService {

    constructor({ baseUrl }) {
        axios.defaults.baseURL = baseUrl;
    }

    setHeader() {
        // axios.defaults.headers.common["Authorization"] = `Token ${JwtService.getToken()}`;
    }

    async query(resource, params) {
        return await axios.get(`${resource}`, params);
    }

    async get(resource, slug = "") {
        try {
            return await axios.get(`${resource}/${slug}`);
        } catch (error) {
            throw new Error(`[RWV] ApiService ${error}`);
        }
    }

    async post(resource, params) {
        return await axios.post(`${resource}`, params);
    }

    update(resource, slug, params) {
        return axios.put(`${resource}/${slug}`, params);
    }

    put(resource, params) {
        return axios.put(`${resource}`, params);
    }

    delete(resource) {
        return axios.delete(resource);
    }
}

export default ApiService;