import { api } from "../services";
import { defineStore } from 'pinia';

export const useLinkStore = defineStore('links', {

    state: () => ({
        token: '',
    }),

    getters: {
        getShortLink(state) {
            return 'http://127.0.0.1:5173/' + state.token;
        },
    },

    actions: {
        async generateShortLink(longLink) {
            const response = await api.post('/links/', { link: longLink })
            if (!!response.data) {
                this.token = response.data
            }
        },
    },
})