<template>
  <div class="team_member">
    <div class="team_member__photo" :style="`background-image: url(../../${photo}.png)`"></div>
    <div class="team_member__name">{{name}}</div>
  </div>
</template>

<style lang="scss">

  .team_member{
    display: flex;
    align-items: center;
    width: 100%;
    height: 30px;
    margin: 10px 0;
    position: relative;
    font-size: 20px;
    color: black;

    .team_member__photo{
      margin-right: 10px;
      background-position: center;
      background-size: contain;
      background-repeat: no-repeat;
      height: 30px;
      width: 30px;
      border-radius: 50%;
    }

    &:after{
      cursor: pointer;
      content: '...';
      position: absolute;
      right: 0;
      font-size: 30px;
      margin-bottom: 17px;
    }
  }

</style>

<script type="text/javascript">
  export default{
    props: ['name', 'photo']
  }
</script>
