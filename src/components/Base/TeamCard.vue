<template>
  <div class="team_card">

    <h2 class="team_card__name">{{name}}</h2>

    <BaseCardProjects :projects="projects"></BaseCardProjects>
    <BaseTeamMembersShort :members="members"></BaseTeamMembersShort>


  </div>
</template>

<style lang="scss">
  .team_card{
    height: 450px;
    width: 320px;
    border-radius: 20px;

    background: #303030;
    box-shadow: 0px 4px 0px #FFD15C;
    border-radius: 32px;
    padding: 30px 20px;
    margin: 0 20px;

    display: flex;
    justify-content: space-between;
    flex-direction: column;

    .team_card__name{
      color: #FFD15C;
      text-transform: uppercase;
      font-size: 32px;
      text-align: left;
      margin: 0;
    }

  }
</style>

<script type="text/javascript">

import BaseTeamMembersShort from './BaseTeamMembersShort.vue'
import BaseCardProjects from './BaseCardProjects.vue'

  export default{
    components:{
      BaseTeamMembersShort,
      BaseCardProjects
    },
    props: ['members', 'name', 'projects']
  }
</script>
