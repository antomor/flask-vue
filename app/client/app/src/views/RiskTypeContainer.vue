<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Risk type - {{riskType ? riskType.name : ''}}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          <p>
            {{riskType ? riskType.description : '' }}
          </p>

          <div v-if="hasFields">
            <field-container class="field" v-for="field in fields" :key="field.id" :field="field"></field-container>
            
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-link">Submit</button>
              </div>
              <div class="control">
                <button class="button is-text">Cancel</button>
              </div>
            </div>
          </div>
          <div v-if="!hasFields">
            No fields saved
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

import FieldContainer from '../components/FieldContainer'

export default {
  name: 'RiskTypeContainer',
  components: {
    'field-container': FieldContainer
  },
  data () {
    const res = { 'riskType': { 'description': 'Risk linked to a vehicle', 'fields': [ { 'id': 1, 'name': 'person age', 'type': 'number', 'value': '23' }, { 'id': 2, 'name': 'address', 'type': 'text', 'value': 'Regent street, London' }, { 'id': 3, 'name': 'birth_date', 'type': 'date', 'value': '2018-01-23' }, { 'id': 4, 'name': 'sex', 'type': 'enum_sex', 'value': 'F' } ], 'id': 1, 'name': 'automobile' } }
    return {
      res: res
    }
  },
  computed: {
    resource () {
      return this.$store.state.resource
    },
    riskType () {
      if (this.resource) {
        return this.resource.riskType
      }
      return null
    },
    hasFields () {
      return this.riskType && this.riskType.fields && this.riskType.fields.length > 0
    },
    fields () {
      return this.riskType.fields
    }
  },
  methods: {
    someMethod () {
      // Do Something
    }
  },
  mounted () {
    this.$store.dispatch('fetchRiskType', this.$route.params.id)
  }
}
</script>

<style lang="sass" scoped>

</style>
