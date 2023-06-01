import { api, userInfo } from "../services";
import { defineStore } from 'pinia';

export const useRedirectStore = defineStore('redirect', {

    state: () => ({
        longLink: null,
    }),

    actions: {
        async getLongLink(token) {
            const response = await api.query('/links/' + token, { params: { only_link: true } })
            this.longLink = response.data
        },

        async addClick(token) {
            const userIP = await userInfo.getUserIP();
            await api.post('/links/' + token, { params: { token: token, user_ip: userIP }})
        }
    }
})