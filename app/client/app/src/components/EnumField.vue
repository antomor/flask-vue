<template>
  <div class="field">
    <label class="label">{{field.name}}: {{field.type}}</label>
    <div class="control">
      <div class="select">
        <select>
          <option v-for="(enumValue, idx) in field.enumValues" :key="idx" :value="field.value" :selected="enumValue === field.value ? 'selected': ''">
            {{ enumValue }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'EnumField',
  props: {
    'field': {type: Object}
  }
}
</script>

<style lang="sass" scoped>

</style>


