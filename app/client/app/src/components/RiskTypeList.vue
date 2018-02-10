<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Risk type list
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          <div v-if="!isEmpty">
            <div class="columns">
              <risk-type-item v-for="riskType in riskTypes" :key="riskType.id" :riskType="riskType"></risk-type-item>
            </div>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

import RiskTypeItem from './RiskTypeItem'

export default {
  name: 'RiskTypeList',
  components: {
    'risk-type-item': RiskTypeItem
  },
  data () {
    return {
    }
  },
  computed: {
    resource () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resource
    },
    riskTypes () {
      return this.resource.riskTypes
    },
    isEmpty () {
      return !this.resource || !this.resource.riskTypes || this.resource.riskTypes.length === 0
    }
  },
  mounted () {
    this.$store.dispatch('fetchRiskTypes')
  }
}
</script>

<style lang="sass" scoped>


</style>
