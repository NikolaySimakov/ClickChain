import { api } from "../services";

const state = {
    longLink: null,
}

const getters = {
    longLink(state) {
        return state.longLink;
    },
}

const actions = {
    async getLongLink({ commit }, token) {
        await api.query('/links/', { params : { token: token }}).then(function (response) {
            const link = response.data;
            commit('GET_LONG_LINK', link);
        });
    },
}

const mutations = {
    GET_LONG_LINK(state, link) {
        state.longLink = link;
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}