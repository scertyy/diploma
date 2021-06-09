<template>
    <div class="index">

        <div class="index__tasks-row">
            <BaseTaskCard class="base-task-card_blue" total_number="51" status="Today"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_yellow" total_number="32" today="46" last_week="2" status="In progress"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_red" total_number="46" today="12" last_week="3" status="Signing</br>a contract"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_green" total_number="113" today="44" last_week="7" status="Сompleted"></BaseTaskCard>
        </div>

        <div class="index__left_block">

          <div class="index__left_block__heading">Colleagues online</div>

          <div class="index__left_block__colleagues">

            <div
              class="index__left_block__colleagues__colleague"
              v-for="(colleague, index) in colleagues"
              :key="index"
            >
              <ColleaguePhoto class="colleague_photo__online" name="roman"></ColleaguePhoto>

              <div class="index__left_block__colleagues__colleague_name">Roman</div>

            </div>

          </div>

          <div class="index__left_block__heading">Recent feed</div>

          <div class="index__left_block__recent_feed">

            <div
              class="recent_feed__feed"
              v-for="(feed, index) in feeds"
              :key="index"
            >

              <ColleaguePhoto :name="feed.first_name"></ColleaguePhoto>

              <div class="feed__text_block">
                <div class="feed_name">{{feed.name}}</div>
                <div class="feed_time">{{feed.time}}</div>
                <div class="feed_comment">{{feed.comment}}</div>
              </div>

            </div>

          </div>

        </div>

        <div class="circles">
          <Circle
            v-for="circle in circles"
            :key="circle.name"
            :percent="circle.percent"
            :cirlce_name="circle.name"
          >

          </Circle>
        </div>
    </div>
</template>

<script>
    import BaseTaskCard from '../../components/Base/BaseTaskCard';
    import ColleaguePhoto from '../../components/Base/ColleaguePhoto';
    import Circle from '../../components/Base/Circle';
    import {useProfile} from "../../composition/useProfile";

    import {onMounted} from 'vue';
    export default {
        components: {
            BaseTaskCard,
            ColleaguePhoto,
            Circle
        },
        setup() {

            const {getProfile} = useProfile()

            onMounted(() => {
                getProfile()
            })

            return {}

        },
        data(){
          return{
            colleagues: 8,
            feeds:[
              {
                name: 'Roman Khmelev',
                first_name: 'roman',
                time: '10:23pm',
                comment: 'Added new clients (x2)'
              },
              {
                name: 'Kirill Kosyrev',
                first_name: 'kirill',
                time: '10:12pm',
                comment: 'Edited info (Case 3)'
              },
              {
                name: 'Roman Khmelev',
                first_name: 'roman',
                time: '10:01pm',
                comment: 'Added new clients (x1)'
              },
            ],
            circles:[
              {
                name: 'Daily plan',
                percent: '93',
              },
              {
                name: 'Weekly plan',
                percent: '75',
              },
              {
                name: 'Monthly plan',
                percent: '25',
              },
              {
                name: 'Year plan',
                percent: '15',
              },
            ]
          }
        }
    }
</script>

<style lang="scss" src="./index.scss"></style>
