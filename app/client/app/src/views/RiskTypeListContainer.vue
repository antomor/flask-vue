<template>
  <section>

    <div class="container">
      <risk-type-list :data="'DataFromParent'"/>
    </div>
  </section>
</template>
<script>
import RiskTypeList from '../components/riskTypeList'

export default {
  name: 'RiskTypeListContainer',
  components: {
    'risk-type-list': RiskTypeList
  },
  data () {
    return {

    }
  },
  computed: {
    isLoading () {
      return this.$store.state.isLoading
    }
  }
}
</script>

<style lang="sass" scoped>

</style>
