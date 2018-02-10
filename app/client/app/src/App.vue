<template>
<div>

    <nav>
        <router-view name="navbar"></router-view>
        <router-view name="hero"></router-view>
        <router-view name="subnavbar"></router-view>
    </nav>
    

    <section class="section">
      <transition name="fade">
        <div class="container">

          <router-view name="main"></router-view>

        </div>
      </transition>
    </section>
    <custom-footer />
</div>
</template>

<script>

import Footer from './components/Footer'

export default {
  name: '',
  components: {
    'custom-footer': Footer
  },
  computed: {
    isLoading () {
      return this.$store.state.isLoading
    }
  }
}
</script>

<style lang="sass">
// Main.sass is imported into all Components using Webpack Data Parameter

</style>
