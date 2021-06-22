<template>
    <div
      class="base-circle-icon"
      :style="{'background': `url(${src}) center / cover no-repeat`}"
    >
    </div>
</template>

<script>
    import {computed, } from 'vue';
    export default {
        props: {
            src: String,
        },
        setup(props) {

            return {
                src: computed(() => props.src),
            }
        }
    }
</script>

<style lang="scss">
  .base-circle-icon{
    width: 58px;
    height: 58px;
    border-radius: 20px 10px 20px 10px;
    position: relative;
      flex-shrink: 0;
      &.base-circle-icon_big {
          width: 256px;
          height: 256px;
          border-radius: 60px 30px 60px 30px;
      }
      &.base-circle-icon_mr-20 {
          margin-right: 20px;
      }
  }
</style>


