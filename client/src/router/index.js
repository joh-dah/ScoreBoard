import { createRouter, createWebHistory } from 'vue-router'
import ScoreBoard from '../components/ScoreBoard.vue'
import Games from '../components/Games.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/scoreboard/:gameId',
      name: 'scoreboard',
      component: ScoreBoard
    },
    {
      path: '/games',
      name: 'games',
      component: Games
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/games'
    }
  ]
})

export default router