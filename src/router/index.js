import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import First from "../views/First.vue";
import Exist from "../views/OldTeam.vue";
import Contact from "../views/Contact.vue";
import Mi from "../views/mi.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "first",
    component: First
  },
  {
    path: "/newteam",
    name: "home",
    component: Home
  },
  {
    path: "/exist",
    name: "exist",
    component: Exist
  },
  {
    path: "/contact",
    name: "contact",
    component: Contact
  },
  {
    path:"/mi",
    name: "mi",
    component: Mi
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
