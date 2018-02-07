import Vue from 'vue'
import backend from './backend'

export default {

  fetchRiskTypes: function (context) {
    backend.fetchRiskTypes().then((responseData) => {
      context.commit('setResource', responseData)
    })
  },

  fetchRiskType: function  (context, resourceId) {
    backend.fetchRiskType(resourceId).then((responseData) => {
      context.commit('setResource', responseData)
    })
  }
}
