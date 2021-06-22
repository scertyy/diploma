<template>
  <div class="team-member">
    <div class="team-member__photo-cont"

    >
      <div class="team-member__photo" :style="`background: url(${member.profile.avatar}) center center / cover no-repeat`"></div>
      <div class="team-member__level">
        {{member.profile.level}}
      </div>
    </div>
    <div class="team-member__name"><span>{{member.position.name}}</span> - {{member.profile.last_name}} {{member.profile.first_name}} </div>
    <div class="team-member__settings-button" @click="openSettingsContributor(member)">...</div>
  </div>
</template>

<script type="text/javascript">
  export default {
    props: {
      member: Object,
    },
    setup(props, {emit}) {


      return {
        member: props.member,
        openSettingsContributor: (member) => emit('openSettingsContributor', member)
      }
    }
  }
</script>

<style lang="scss">

  .team-member{
    display: flex;
    align-items: center;
    width: 100%;
    margin: 10px 0;
    position: relative;
    font-size: 20px;
    color: black;
  }
  .team-member__photo-cont{
    margin-right: 10px;
    height: 30px;
    width: 30px;
    border-radius: 50%;
    .team-member__photo {
      height: 30px;
      width: 30px;
      border-radius: 50%;
    }
    .team-member__level {
      display: none;
      height: 30px;
      width: 30px;
      border-radius: 50%;
      border: 2px solid rgba(255, 209, 92, 0.93);
    }
    &:hover {
      .team-member__photo {
        display: none;
      }
      .team-member__level {
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
  }
  .team-member__name {
    text-align: left;
    span {
      font-weight: bold;
    }
  }
  .team-member__settings-button{
    cursor: pointer;
    content: '...';
    right: 0;
    font-size: 30px;
    margin-bottom: 17px;
    margin-left: auto;
  }

</style>


