<template>
  <div class="team-card">

    <h2 class="team-card__name">{{name}}</h2>

    <BaseCardProjects :projects="projects"></BaseCardProjects>
    <BaseTeamMembersShort :members="members"></BaseTeamMembersShort>


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
    props: ['members', 'name', 'projects']
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

    display: flex;
    justify-content: space-between;
    flex-direction: column;

    .team-card__name{
      color: #FFD15C;
      text-transform: uppercase;
      font-size: 32px;
      text-align: left;
      margin: 0;
    }

  }
</style>


