import { api } from "../services";
import { defineStore } from 'pinia';
import { CONFIG } from '../config';

export const useLinkStore = defineStore('links', {

    state: () => ({
        token: '',
    }),

    getters: {
        getShortLink(state) {
            return CONFIG.DOMAIN + state.token;
        },
    },

    actions: {
        async generateShortLink(longLink) {
            const response = await api.post('/links/', { params: { link: longLink }})
            if (!!response.data) {
                this.token = response.data
            }
        },
    },
})