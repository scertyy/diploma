import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import(/* webpackChunkName: "about" */ '../views/index/index.vue'),
    meta: {
      requiredAuth: true,
      header: 'Главная'
    }
  },
  {
    path: '/tasks',
    name: 'tasks',
    component: () => import(/* webpackChunkName: "about" */ '../views/tasks/tasks.vue'),
    meta: {
      requiredAuth: true,
      header: 'Задачи'

    }
  },
  {
    path: '/teams',
    name: 'teams',
    component: () => import(/* webpackChunkName: "about" */ '../views/teams/teams.vue'),
    meta: {
      requiredAuth: true,
      header: 'Команды'
    }
  },
  {
    path: '/team',
    name: 'team',
    component: () => import(/* webpackChunkName: "about" */ '../views/team/team.vue'),
    meta: {
      requiredAuth: true,
      header: 'Команда'
    },
    children: [
      {
        path: ':id',
        component: () => import(/* webpackChunkName: "about" */ '../views/team/id/team-id'),
        meta: {
          requiredAuth: true,
          header: 'Команда'
        },
      }
    ]
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import(/* webpackChunkName: "about" */ '../views/settings/settings.vue'),
    meta: {
      requiredAuth: true,
      header: 'Настройки'
    }
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import(/* webpackChunkName: "about" */ '../views/auth/auth.vue'),
    meta: {
      header: 'Авторизация'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
