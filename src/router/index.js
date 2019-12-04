import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import NewGroup from "../views/NewGroup.vue";
import ExistingGroup from "../views/ExistingGroup.vue";
import Contact from "../views/Contact.vue";
<<<<<<< HEAD
import About from "../views/About.vue";
=======
import Mi from "../views/mi.vue";
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
<<<<<<< HEAD
    path: "/newgroup",
    name: "newgroup",
    component: NewGroup
  },
  {
    path: "/existing",
    name: "existing",
    component: ExistingGroup
=======
    path: "/exist",
    name: "exist",
    component: Exist
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee
  },
  {
    path: "/contact",
    name: "contact",
    component: Contact
  },
  {
<<<<<<< HEAD
    path: "/about",
    name: "about",
    component: About
=======
    path:"/mi",
    name: "mi",
    component: Mi
>>>>>>> b768921fa4cc6f34c95c093d4276eab8d248e7ee
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
