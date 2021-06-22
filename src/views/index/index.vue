<template>
    <div class="index">
        <ProfileInfo :profile="profile"></ProfileInfo>
        <ProfilePlans :circles="circles"></ProfilePlans>

        <div class="index__tasks-row">
            <BaseTaskCard class="base-task-card_blue" total_number="51" status="Запланировано"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_yellow" total_number="32"  status="В процессе"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_red" total_number="46"  status="Заканчивается срок сегодня"></BaseTaskCard>
            <BaseTaskCard class="base-task-card_green" total_number="113" today="44" last_week="7" status="Выполнено"></BaseTaskCard>
        </div>

    </div>
</template>

<script>
    import BaseTaskCard from '../../components/Base/BaseTaskCard';
    import ProfileInfo from '../../components/profile/profileInfo';
    import ProfilePlans from '../../components/profile/profilePlans';
    import {useProfile} from "../../composition/useProfile";

    import {onMounted, ref} from 'vue';
    import {useRouteName} from "../../composition/useRouteName";
    export default {
        components: {
            BaseTaskCard,

            ProfileInfo,
            ProfilePlans
        },
        setup() {

            const {getProfile, profile} = useProfile()
            const { routeName } = useRouteName()

            onMounted(() => {
                getProfile()
                routeName.value = 'Профиль'
            })
            const circles = ref([
                  {
                    name: 'Дневной план',
                    percent: '93',
                  },
                  {
                    name: 'Недельный план',
                    percent: '75',
                  },
                  {
                    name: 'Месячный план',
                    percent: '25',
                  },
                  {
                    name: 'Годовой план',
                    percent: '15',
                  },
                ])

            return {
                profile,
                circles
            }

        },
    }
</script>

<style lang="scss" src="./index.scss"></style>
