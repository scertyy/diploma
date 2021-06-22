<template>
  <div class="project-short">
    <div class="project-short__name">
      <div class="project-short__action__image" :style="`background: url(${subteam.avatar}) center center / cover no-repeat`">
      </div>
      {{subteam.name}}
    </div>
    <div class="project-short__action">{{subteam.description}}</div>
    <div class="project-short__creator">
      <div class="project-short__creator__photo"
           v-for="contributor in subteam.contributors"
           :style="`background: url(${contributor.profile.avatar}) center center / cover no-repeat`" >

      </div>
    </div>
    <div class="project-short__action-button">...</div>

  </div>
</template>

<script type="text/javascript">
  export default{
    props: {
      subteam: Object,
    }
  }
</script>

<style lang="scss">
  .project-short{
    width: 100%;
    border-radius: 10px;
    background-color: white;
    margin: 10px 0;
    position: relative;

    display: flex;
    text-align: left;
    align-items: center;
    padding: 15px 0;
  }
  .project-short__name{
    width: 30%;
    padding: 0 20px;
    font-size: 20px;
    font-weight: bold;
    display: flex;
    align-items: center;
  }

  .project-short__creator{
    width: 30%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    position: relative;
  }
  .project-short__creator__photo{
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-position: center;
    background-size: contain;
    background-repeat: no-repeat;
    left: 0;
    flex-shrink: 0;
    margin-right: 3px;
    &:last-of-type {
      margin-right: 0;
    }
  }

  .project-short__action{
    width: 30%;
    display: flex;
    align-items: center;
    position: relative;


  }
  .project-short__action__image{
    width: 25px;
    height: 25px;
    border-radius: 50%;
    flex-shrink: 0;
    margin-right: 15px;
  }
  .project-short__action-button{
    width: 10%;
    text-align: right;
    cursor: pointer;
    font-size: 30px;
    margin: 0 16px 17px 0;
  }
</style>


