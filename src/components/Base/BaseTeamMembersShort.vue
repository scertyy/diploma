
<template>
  <div class="base-team-members-short">
    <h4 class="base-team-members-short__members-head">Участники</h4>
    <div class="base-team-members-short__members-photos">
      <div class="base-team-members-short__member-photo"
        v-for="member in members"
        :key="member.profile.avatar"
        :style="`background: url(${member.profile.avatar}) center / cover no-repeat`"
      ></div>

      <div class="base-team-members-short__member-add" @click="add">+</div>
    </div>
  </div>
</template>

<script>
  import {computed} from 'vue';
  export default{
    props: {
      members: Array,
    },
    setup(props, {emit}) {

      return {
        members: computed(() => props.members),
        add: () => emit('add'),
      }
    }
  }
</script>


<style lang="scss">

  .base-team-members-short{
    color: white;
    width: 100%;
    border-radius: 5px;
    padding: 5px 0;

    .base-team-members-short__members-photos{
      display: flex;
      height: 30px;
      margin: 0px 10px;

      .base-team-members-short__member-add{
        color: #FFD15C;
        font-size: 26px;
        line-height: 120%;
        cursor: pointer;
        display: none;
      }
    }

    .base-team-members-short__members-head{
      color: rgb(144, 144, 144);
      text-align: left;
      margin-bottom: 10px;
    }

    .base-team-members-short__member-photo{
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

  .base-team-members-short_modal {
    padding: 0 20px;

    .base-team-members-short__members-head{
      color: white;
      font-size: 22px;
      text-align: left;
      margin-bottom: 10px;
    }

    .base-team-members-short__members-photos{
      .base-team-members-short__member-add{
        display: block;
      }
    }
  }

  .base-team-members-short__edit-task-modal {

    .base-team-members-short__members-head{
      color: white;
      font-size: 22px;
      text-align: left;
      margin: 0;
      display: none;
    }

    .base-team-members-short__members-photos{
      .base-team-members-short__member-add{
        display: block;
        margin: 0 10px;
      }
    }
  }
</style>

