<template>
  <div class="team-card" >
    <div class="team-card__opacity-color" :style="team.avatar ? {
      'background': `url(${team.avatar}) center center / cover no-repeat`
  } : {  }"></div>
    <div class="team-card__container">
      <router-link :to="`/team/${team.id}`" class="team-card__name">{{team.name}}</router-link>
      <BaseCardProjects :projects="team.sub_teams"></BaseCardProjects>

      <BaseTeamMembersShort :members="team.contributors"></BaseTeamMembersShort>
    </div>

  </div>
</template>

<script type="text/javascript">

  import BaseTeamMembersShort from './BaseTeamMembersShort.vue'
  import BaseCardProjects from './BaseCardProjects.vue'

  export default{
    components:{
      BaseTeamMembersShort,
      BaseCardProjects
    },
    props: {
      team: Object
    },
    setup(props) {

      return {
        team: props.team
      }
    }
  }
</script>

<style lang="scss">
  .team-card{
    height: 450px;
    width: 320px;

    background: #303030;
    box-shadow: 0px 4px 0px #FFD15C;
    border-radius: 48px 24px;
    padding: 30px 20px;
    margin: 20px;
    position: relative;

    display: flex;
    justify-content: space-between;
    flex-direction: column;

    .team-card__name{
      color: #FFD15C;
      text-transform: uppercase;
      font-size: 32px;
      text-align: left;
      margin: 0;
      text-decoration: none;
    }

  }
  .team-card__opacity-color {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: .1;
    left: 0;
    top: 0;
    border-radius: 48px 24px;
    z-index: 0;
  }
  .team-card__container {
    width: 100%;
    height: 100%;
    position: relative;
    background: transparent;
    text-align: left;
  }
</style>


