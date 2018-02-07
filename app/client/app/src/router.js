import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'

import RiskTypeListContainer from './views/RiskTypeListContainer'
import RiskTypeContainer from './views/RiskTypeContainer'
import Login from './views/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      components: {
        main: Login
      }
    },
    {
      path: '/risk-types',
      name: 'riskTypes',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: RiskTypeListContainer
      }
    },
    {
      path: '/risk-type/:id',
      name: 'riskTypeItem',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: RiskTypeContainer
      },
      props: {
        navbar: false,
        subnavbar: false,
        main: true
      }
    }
  ]
})
