import { createRouter, createWebHistory } from 'vue-router';

import Link from '../pages/Link.vue';
import Detail from '../pages/Detail.vue';
import Redirect from '../pages/Redirect.vue';

const routes = [
    { path: '/', component: Link },
    { path: '/:token', component: Redirect },
    { path: '/:token/detail', component: Detail },
]

export default createRouter({
    history: createWebHistory(),
    routes: routes
});