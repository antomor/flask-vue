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
            <ul>
              <risk-type-item v-for="riskType in riskTypes" :key="riskType.id" :riskType="riskType"></risk-type-item>
            </ul>
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
    const res = { 'riskTypes': [ { 'description': 'Risk linked to a vehicle', 'fields': [ { 'id': 1, 'name': 'person age', 'type': 'number', 'value': '23' }, { 'id': 2, 'name': 'address', 'type': 'text', 'value': 'Regent street, London' }, { 'id': 3, 'name': 'birth_date', 'type': 'date', 'value': '01/23/2018' }, { 'id': 4, 'name': 'sex', 'type': 'sex', 'value': 'F' } ], 'id': 1, 'name': 'automobile' }, { 'description': 'Risk linked to a house', 'fields': [ { 'id': 5, 'name': 'person age', 'type': 'number', 'value': '23' }, { 'id': 6, 'name': 'address', 'type': 'text', 'value': 'Regent street, London' }, { 'id': 7, 'name': 'birth_date', 'type': 'date', 'value': '01/23/2018' }, { 'id': 8, 'name': 'sex', 'type': 'sex', 'value': 'F' } ], 'id': 2, 'name': 'house' } ] }
    return {
      res: res
    }
  },
  computed: {
    resource () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resource
    },
    riskTypes () {
      return this.res.riskTypes
    },
    isEmpty () {
      return !this.res.riskTypes || this.res.riskTypes.length === 0
    }
  },
  mounted () {
    this.$store.dispatch('fetchRiskTypes')
  }
}
</script>

<style lang="sass" scoped>


</style>
