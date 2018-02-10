<template>
<div class="column">
  <router-link :to="{ name: 'riskTypeItem', params:{id:riskType.id}}">
    <div class="card">
    <header class="card-header">
    <p class="card-header-title">
      {{riskType.name}}
    </p>
  </header>
  <div class="card-content">
    <div class="media">
      <div class="media-content">
        <p class="title is-4">{{riskType.name}}</p>
        <p class="subtitle is-6">{{riskType.description}}</p>
      </div>
    </div>

    <div class="content">
      <div v-for="field in riskType.fields" :key="field.id">
        {{field.name}} - {{field.value}}
      </div>
      
    </div>
  </div>
</div>
  </router-link>
  
</div>
  
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