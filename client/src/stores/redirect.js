import { api } from "../services";
import { defineStore } from 'pinia';

export const useRedirectStore = defineStore('redirect', {

    state: () => ({
        longLink: null,
    }),

    actions: {
        async getLongLink(token) {
            const response = await api.query('/links/', { params: { token: token } })
            this.longLink = response.data
        },
    }
})