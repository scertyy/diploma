<template>
    <div class="month">

    </div>
    <div class="weekdays">

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
    props: ['name'],

    data(){
      return(){
        weekdays: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        days: 31
      }
    }
  }
</script>
