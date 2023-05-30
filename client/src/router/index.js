import { createRouter, createWebHistory } from 'vue-router';

import Link from '../pages/Link.vue';
import Detail from '../pages/Detail.vue';
import Redirect from '../pages/Redirect.vue';
import Login from '../pages/account/Login.vue';
import Signin from '../pages/account/Signin.vue';

const routes = [
    { path: '/', component: Link },
    { path: '/:token', component: Redirect },
    { path: '/:token/detail', component: Detail },
    { path: '/login', component: Login },
    { path: '/signin', component: Signin },
]

export default createRouter({
    history: createWebHistory(),
    routes: routes
});