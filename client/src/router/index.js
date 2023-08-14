import { createRouter, createWebHistory } from 'vue-router';

import Link from '../pages/Link.vue';
import Detail from '../pages/Detail.vue';
import Redirect from '../pages/Redirect.vue';
import Signup from '../pages/account/Signup.vue';
import Signin from '../pages/account/Signin.vue';

const routes = [
    { path: '/', component: Link },
    { path: '/:token', component: Redirect },
    { path: '/:token/detail', component: Detail },
    { path: '/signup', component: Signup },
    { path: '/signin', component: Signin },
]

export default createRouter({
    history: createWebHistory(),
    routes: routes
});