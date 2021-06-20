<template>
    <div class="base-task-card">

      <div class="base-task-card__head">
        <div class="base-task-card__head__tasks_number">{{total_number}}</div>
        <div class="base-task-card__head__status" v-html="status"></div>
      </div>

      <div class="base-task-card__bottom">
        <div v-if="today" class="base-task-card__bottom__today">{{today}} сегодня</div>
        <div v-if="last_week" class="base-task-card__bottom__last_week">{{last_week}} за последнюю неделю</div>
      </div>

    </div>
</template>

<style lang="scss">
    .base-task-card {
        background: #303030;

        border-radius: 32px;

        width: 331px;
        height: 344px;
        padding: 25px;

        color: white;
        text-align: left;
        font-size: 20px;

        display: flex;
        flex-direction: column;
        justify-content: space-between;

        .base-task-card__head__tasks_number{
          font-weight: bold;
          font-size: 72px;
          line-height: 120%;
        }

        .base-task-card__head__status{
          font-weight: bold;
          font-size: 36px;
        }

        .base-task-card__bottom__last_week{
          color: #A7A7A7;
        }

        &.base-task-card_blue {
            box-shadow: 0px 4px 0px #48D1FD;

            .base-task-card__head__tasks_number{
              color: #48D1FD;
            }
        }
        &.base-task-card_yellow {
            box-shadow: 0px 4px 0px #FFD15C;

            .base-task-card__head__tasks_number{
              color: #FFD15C;
            }
        }
        &.base-task-card_red {
            box-shadow: 0px 4px 0px #E2626A;

            .base-task-card__head__tasks_number{
              color: #E2626A;
            }
        }
        &.base-task-card_green {
            box-shadow: 0px 4px 0px #4CCE59;

            .base-task-card__head__tasks_number{
              color: #4CCE59;
            }
        }
    }
</style>

<script type="text/javascript">
  export default {
    props: ['status', 'total_number', 'today', 'last_week']
  }
</script>
