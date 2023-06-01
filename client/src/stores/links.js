import { api } from "../services";
import { defineStore } from 'pinia';
import { CONFIG } from '../config';

export const useLinkStore = defineStore('links', {

    state: () => ({
        token: '',
        links: [],
    }),

    getters: {
        getShortLink(state) {
            return CONFIG.DOMAIN + state.token;
        },
        getHistory(state) {
            return state.links;
        },
    },

    actions: {
        async generateShortLink(longLink) {
            const response = await api.post('/links/', { params: { link: longLink }})
            if (!!response.data) {
                this.token = response.data
            }
        },

        async getLinksHistory() {
            const response = await api.query('/links/')
            if (!!response.data) {
                this.links = response.data;
                this.links.forEach(link => {
                    api.query('/statistics/' + link.token + '/clicks', { params : { additional_settings : 'count' }}).then(resp => {
                        Object.assign(link, { clicks: resp.data })
                    })
                })
            }
        },

    },
})