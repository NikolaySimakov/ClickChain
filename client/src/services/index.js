import { CONFIG } from '../config';
import ApiService from './api';

export const api = new ApiService({
    baseUrl: CONFIG.API_HOST,
});