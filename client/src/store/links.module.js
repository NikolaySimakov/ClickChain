import { api } from "../services";

const state = {
    token: null,
}

const getters = {
    getShortLink(state) {
        return 'http://127.0.0.1:5173/' + state.token;
    },
    
}

const actions = {
    async generateShortLink({ commit }, longLink) {
        await api.post('/links/', { link: longLink }).then(function (response) {
            const token = response.data
            if (!!response.data) commit('GENERATE_SHORT_LINK', token);
        });
    },
}

const mutations = {
    GENERATE_SHORT_LINK(state, token) {
        state.token = token;
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}