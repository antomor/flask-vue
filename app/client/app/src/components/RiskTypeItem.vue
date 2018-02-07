<template>
  <router-link tag="li" activeClass='is-active' :to="{ name: 'riskTypeItem', params:{id:riskType.id}}">
    <a>
      {{riskType.name}} - {{riskType.description}}
      <span class="is-size-7 has-text-grey-light">{{riskType.id}}</span>
    </a>
  </router-link>
</template>

<script>

export default {
  name: 'RiskTypeItem',
  props: {
    'riskType': {type: Object}
  },
  data () {
    return {}
  }
}
</script>


<style lang="sass" scoped>


</style>