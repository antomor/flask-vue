<template>
    <div class="field">
        <text-field v-if="isText" :field="field" />
        <number-field v-if="isNumber" :field="field" />
        <date-field v-if="isDate" :field="field" />
        <enum-field v-if="isEnum" :field="field" />
        <text-field v-if="isOther" :field="field" />
    </div>
</template>
<script>

import TextField from './TextField'
import NumberField from './NumberField'
import DateField from './DateField'
import EnumField from './EnumField'

export default {
  name: 'FieldContainer',
  components: {
    'text-field': TextField,
    'number-field': NumberField,
    'date-field': DateField,
    'enum-field': EnumField
  },
  props: {
    'field': {type: Object}
  },
  computed: {
    isText () {
      return this.field.type === 'text'
    },
    isNumber () {
      return this.field.type === 'number'
    },
    isDate () {
      return this.field.type === 'date'
    },
    isEnum () {
      return this.field.type.startsWith('enum')
    },
    isOther () {
      return !this.isText &&
        !this.isNumber &&
        !this.isDate &&
        !this.isEnum
    }
  }
}
</script>

<style lang="sass" scoped>

</style>


