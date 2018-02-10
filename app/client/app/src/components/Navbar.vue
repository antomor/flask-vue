<template>
  <section class="hero is-primary">
  <div class="hero-body">
    <p class="title">
       <a href="#/">{{title}}</a>
    </p>
    <p class="subtitle">
      {{subtitle}}
    </p>
  </div>
</section>
</template>
<script>

export default {
  name: 'Navbar',
  data () {
    return {
      title: 'Flask-vue',
      subtitle: 'A sample usage of flask and vue.js'
    }
  }
}
</script>

<style lang="sass" scoped>

nav.navbar
  min-height: none
  background-color: $nav-background
  border-bottom: solid 1px #dbdbdb

.navbar-brand > .navbar-item
  padding-left: 10px

  img
    height: 15px

</style>
