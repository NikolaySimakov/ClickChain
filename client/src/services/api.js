import axios from "axios";

class ApiService {

    constructor({ baseUrl }) {
        axios.defaults.baseURL = baseUrl;
    }

    setHeader() {
        // axios.defaults.headers.common["Authorization"] = `Token ${JwtService.getToken()}`;
    }

    async query(resource, params) {
        try {
            return await axios.get(`${resource}`, params);
        } catch (error) {
            throw new Error(`ApiService ${error}`);
        }
    }

    async get(resource, slug = "") {
        try {
            return await axios.get(`${resource}/${slug}`);
        } catch (error) {
            throw new Error(`ApiService ${error}`);
        }
    }

    async post(resource, params) {
        try {
            return await axios.post(resource, null, params);
        } catch (error) {
            throw new Error(`ApiService ${error}`);
        }
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