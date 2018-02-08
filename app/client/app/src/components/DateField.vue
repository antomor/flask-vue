<template>
    <div class="field">
        <label class="label">{{field.name}} : {{field.type}}</label>
        <div class="control">
        <input class="input" type="date" :value="field.value"> 
        </div>
    </div>
</template>
<script>

export default {
  name: 'DateField',
  props: {
    'field': {type: Object}
  }
}
</script>

<style lang="sass" scoped>

</style>


