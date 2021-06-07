import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Главная',
    component: () => import(/* webpackChunkName: "about" */ '../views/index/index.vue'),
    meta: {
      requiredAuth: true,
    }
  },
  {
    path: '/tasks',
    name: 'Задачи',
    component: () => import(/* webpackChunkName: "about" */ '../views/tasks/tasks.vue'),
    meta: {
      requiredAuth: true,
    }
  },
  {
    path: '/team',
    name: 'Команды',
    component: () => import(/* webpackChunkName: "about" */ '../views/team/team.vue'),
    meta: {
      requiredAuth: true,
    }
  },
  {
    path: '/settings',
    name: 'Настройки',
    component: () => import(/* webpackChunkName: "about" */ '../views/settings/settings.vue'),
    meta: {
      requiredAuth: true,
    }
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import(/* webpackChunkName: "about" */ '../views/auth/auth.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
