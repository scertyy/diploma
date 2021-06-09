<template>
  <div class="project_short">
    <div class="project_short__name">{{name}}</div>
    <div class="project_short__creator">{{creator.name}}
      <div class="project_short__creator__photo" :style="`background-image: url(../../${creator.photo}.png)`"></div>
    </div>
    <div class="project_short__action">{{action.comment}}
      <div class="project_short__action__image" :style="`background-image: url(../../${action.author}.png)`">

      </div>
    </div>
  </div>
</template>

<style lang="scss">
  .project_short{
    width: 100%;
    border-radius: 10px;
    height: 50px;
    background-color: white;
    margin: 10px 0;
    position: relative;

    display: flex;
    text-align: left;
    align-items: center;

    .project_short__name{
      width: 25%;
      padding: 0 20px;
      font-size: 20px;
      font-weight: bold;
    }

    .project_short__creator{
      width: 15%;
      display: flex;
      align-items: center;
      position: relative;
      text-align: left;
      padding: 35px;

      .project_short__creator__photo{
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background-position: center;
        background-size: contain;
        background-repeat: no-repeat;
        position: absolute;
        left: 0;
      }
    }

    .project_short__action{
      width: 60%;
      padding: 0 10px 0 45px;
      display: flex;
      align-items: center;
      position: relative;

      .project_short__action__image{
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background-position: center;
        background-size: contain;
        background-repeat: no-repeat;
        position: absolute;
        left: 10px;
      }
    }

    &:after{
      cursor: pointer;
      content: '...';
      position: absolute;
      right: 20px;
      font-size: 30px;
      margin-bottom: 17px;
    }
  }
</style>

<script type="text/javascript">
  export default{
    props: ['name', 'creator', 'action']
  }
</script>
