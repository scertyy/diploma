import {createRouter, createWebHistory} from 'vue-router'
import index from '../views/index/index.vue'
import services from "../views/services/services.vue";
import doctor from "../views/doctor/doctor.vue";
import review from "../views/review/review.vue";
import contact from "../views/contact/contact.vue";
import cardiology from "../views/services/pages/cardiology.vue";
import endocrinology from "../views/services/pages/endocrinology.vue";
import gastroenterology from "../views/services/pages/gastroenterology.vue";
import gynecology from "../views/services/pages/gynecology.vue";
import laboratory from "../views/services/pages/laboratory.vue";
import neurology from "../views/services/pages/neurology.vue";
import therapy from "../views/services/pages/therapy.vue";
import ultrasound from "../views/services/pages/ultrasound.vue";



import all from "../views/services/pages/all.vue";

const routes = [
    {
        path: '/',
        name: 'index',
        component: index,
    },
    {
        path: '/services/',
        name: 'services',
        component: services,
        children: [
            {
                path: '/services/',
                component: all,
            },
            {
                path: '/services/cardiology',
                component: cardiology,
            },
            {
                path: '/services/endocrinology',
                component: endocrinology,
            },
            {
                path: '/services/gastroenterology',
                component: gastroenterology,
            },
            {
                path: '/services/gynecology',
                component: gynecology,
            },
            {
                path: '/services/laboratory',
                component: laboratory,
            },
            {
                path: '/services/neurology',
                component: neurology,
            },
            {
                path: '/services/therapy',
                component: therapy,
            },
            {
                path: '/services/ultrasound',
                component: ultrasound,
            },
        ]
    },
    {
        path: '/doctor',
        name: 'doctor',
        component: doctor
    },
    {
        path: '/review',
        name: 'review',
        component: review
    },
    {
        path: '/contact',
        name: 'contact',
        component: contact
    },
    {
        path: "/:catchAll(.*)",
        component: index,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
