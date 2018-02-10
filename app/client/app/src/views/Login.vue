<template>
  <section>
    <div class="level login-logo">
     <section class="hero is-medium is-primary is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            {{title}}
          </h1>
          <h2 class="subtitle">
            {{subtitle}}
          </h2>
        </div>
        <div class="level">
      <div class="level-item has-text-centered">
        <router-link tag="a" :to="{ path: 'risk-types'}" class="button">Login</router-link>
      </div>
  </div>
      </div>
    </section>
    </div>
    
</section>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      title: 'Flask-vue',
      subtitle: 'A sample usage of flask and vue.js'
    }
  }
}
</script>

<style lang="sass" scoped>

.login-logo
  margin-top: 100px

  img
    height: 150px

</style>
