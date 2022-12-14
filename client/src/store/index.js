import { createStore } from "vuex";

import links from "./links.module";
import redirect from './redirect.module';


export default createStore({
    modules: {
        links,
        redirect,
    }
})