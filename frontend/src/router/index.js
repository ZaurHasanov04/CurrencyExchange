import {createRouter, createWebHistory } from "vue-router";
import SignUp from "../views/SignUp.vue";
import VerifyOTP from "../views/VerifyOTP.vue";
import Index from "../views/Index.vue";

// import SignUp from "@/components/SignUp.vue";

const routes = [
  {
    path:'/',
    name: 'index',
    component: Index,
  },
  {
    path: "/signup",
    name:'signup',
    component: SignUp,
  },
  {
    path: "/verify_otp",
    name: "VerifyOTP",
    component: VerifyOTP,
    props: true,
  },
];

const router = new createRouter({
    history: createWebHistory(),
    routes
});

export default router;