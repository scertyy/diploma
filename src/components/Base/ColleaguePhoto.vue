<template>
    <div
      class="colleague_photo"
      :style="`background-image: url(./${name}.png)`"
    >
    </div>
</template>

<style lang="scss">
  .colleague_photo{
    width: 58px;
    height: 58px;
    border-radius: 20px 10px 20px 10px;
    position: relative;
  }
</style>

<script type="text/javascript">
  export default {
    props: ['name']
  }
</script>
