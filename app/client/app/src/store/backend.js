import axios from 'axios'


let $backend = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/',
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$backend.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    console.log(error)
    return Promise.reject(error)
  });

export default {

  fetchRiskTypes () {
    return $backend.get(`risk-types/`)
      .then(response => response.data)
  },

  fetchRiskType (resourceId) {
    return $backend.get(`risk-types/${resourceId}`)
      .then(response => response.data)
  }
}
