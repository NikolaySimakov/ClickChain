import { CONFIG } from '../config';
import ApiService from './api';
import userInfo from './userInfo';

const api = new ApiService({
    baseUrl: CONFIG.API_HOST,
});

export {
    api,
    userInfo,
}