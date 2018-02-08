import axios from 'axios'

// let hostUrl = 'http://127.0.0.1:5000/api/';
let hostUrl = 'https://word-nerds-api.herokuapp.com/api';

let $backend = axios.create({
    baseURL: hostUrl,
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
