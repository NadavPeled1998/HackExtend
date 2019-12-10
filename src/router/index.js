import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import NewGroup from "../views/NewGroup.vue";
import ExistingGroup from "../views/ExistingGroup.vue";
import Contact from "../views/Contact.vue";
import About from "../views/About.vue";
import Numbers from "../views/Numbers.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/newgroup",
    name: "newgroup",
    component: NewGroup
  },
  {
    path: "/existing",
    name: "existing",
    component: ExistingGroup
  },
  {
    path: "/contact",
    name: "contact",
    component: Contact
  },
  {
    path: "/about",
    name: "about",
    component: About
  },
  {
    path: "/numbers",
    name: "numbers",
    component: Numbers
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
