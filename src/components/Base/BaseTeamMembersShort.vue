
<template>
  <div class="team_members_short">
    <h4 class="team_members_short__members_head">Участники</h4>

    <div class="team_members_short__members__photos">
      <div class="team_members_short__member_photo"
        v-for="member in members"
        :key="member.photo"
        :style="`background-image: url(../../${member.photo}.png)`"
      ></div>

      <div class="team_members_short__member_add">+</div>
    </div>
  </div>
</template>

<style lang="scss">

  .team_members_short{
    color: white;
    width: 100%;
    border-radius: 5px;
    padding: 5px 0;

    .team_members_short__members__photos{
      display: flex;
      height: 30px;
      margin: 0px 10px;

      .team_members_short__member_add{
        color: #FFD15C;
        font-size: 26px;
        line-height: 120%;
        cursor: pointer;
        display: none;
      }
    }

    .team_members_short__members_head{
      color: rgb(144, 144, 144);
      text-align: left;
      margin-bottom: 10px;
    }

    .team_members_short__member_photo{
      height: 30px;
      width: 30px;
      margin: 0 7px;
      border-radius: 50%;
      background-position: center;
      background-size: contain;
      background-repeat: no-repeat;

      &:nth-of-type(n + 5){
        display: none;
      }
    }
  }

  .team_members_short__modal {

    .team_members_short__members_head{
      color: white;
      font-size: 22px;
      text-align: left;
      margin-bottom: 10px;
    }

    .team_members_short__members__photos{
      .team_members_short__member_add{
        display: block;
      }
    }
  }
</style>

<script type="text/javascript">
  export default{
    props: ['members']
  }
</script>
